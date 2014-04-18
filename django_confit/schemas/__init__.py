"""Schemas for configuration validation."""
import os

import django

from django_confit.utils.importlib import import_member


def get_django_schema_class():
    """Return colander schema class for current (installed) Django version."""
    schema_import_path = \
        'django_confit.schemas.django_{major}_{minor}' \
        '.Django{major}_{minor}_{micro}ConfigurationSchema' \
        .format(
            major=django.VERSION[0],
            minor=django.VERSION[1],
            micro=django.VERSION[2])
    try:
        return import_member(schema_import_path)
    except ImportError as e:
        raise ImportError(
            'Could not import "{schema_path}". '
            'Django version {version} is not supported by django_confit. \n'
            '{exception}'
            .format(
                schema_path=schema_import_path,
                version=django.get_version(),
                exception=e,
            )
        )


DjangoConfigurationSchema = get_django_schema_class()


def guess_project():
    """Return project's package name, computed from DJANGO_SETTINGS_MODULE.

    >>> os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
    >>> guess_project()
    'myproject'

    >>> os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.demo.settings'
    >>> guess_project()
    'myproject.demo'

    >>> os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    >>> guess_project()
    ''

    """
    parts = os.environ.get('DJANGO_SETTINGS_MODULE', '').split('.')
    if parts:
        parts.pop()
        return '.'.join(parts)


def composite_schema_class(installed_apps):
    """Return colander schema class for current Django and installed apps.

    Tries to automatically load schemas of applications either implemented by
    project (local overrides), or by apps themselves, or by django_confit:

    1. ``<PROJECT>.settings_schemas.<APP>.ConfigurationSchema`` where
       ``<PROJECT>`` is the package part of ``DJANGO_SETTINGS_MODULE``
       environment variable.

    2. ``<APP>.settings_schemas.ConfigurationSchema``

    3. ``django_confit.schemas.<APP>.ConfigurationSchema``

    """
    bases = [DjangoConfigurationSchema]
    project = guess_project()
    for app in installed_apps:
        locations = []
        if project:
            locations.append(
                '{project}.settings_schemas.{app}.ConfigurationSchema'
                .format(app=app, project=project))
        locations.append(
            '{app}.settings_schemas.ConfigurationSchema'.format(app=app))
        locations.append(
            'django_confit.schemas.{app}.ConfigurationSchema'.format(app=app))
        for schema_path in locations:
            try:
                bases.append(import_member(schema_path))
            except ImportError:
                pass
            else:
                break
    return type('CompositeConfigurationSchema', tuple(bases), {})


def composite_schema(installed_apps):
    """Return schema instance using ``installed_apps``."""
    schema_class = composite_schema_class(installed_apps)
    return schema_class()


def validate_settings(raw_settings):
    """Return cleaned settings using schemas collected from INSTALLED_APPS."""
    # Perform early validation on Django's INSTALLED_APPS.
    django_schema = DjangoConfigurationSchema()
    django_settings = django_schema.deserialize(raw_settings)
    # Create schema instance using INSTALLED_APPS.
    settings_schema = composite_schema(
        installed_apps=django_settings['INSTALLED_APPS'])
    # Return cleaned settings.
    return settings_schema.deserialize(raw_settings)
