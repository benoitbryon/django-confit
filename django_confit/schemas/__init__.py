"""Schemas for configuration validation."""
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


def composite_schema_class(installed_apps, mapping={}):
    """Return colander schema class for current Django and installed apps.

    Tries to load schemas of applications as mentioned in ``mapping`` or
    builtin django_confit:

    1. ``mapping[<APP>]``

    2. ``django_confit.schemas.<APP>.ConfigurationSchema``

    """
    bases = [DjangoConfigurationSchema]
    for app in installed_apps:
        locations = []
        try:
            locations.append(mapping[app])
        except KeyError:
            pass
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


def composite_schema(installed_apps, mapping={}):
    """Return schema instance using ``installed_apps``."""
    schema_class = composite_schema_class(installed_apps, mapping)
    return schema_class()


def validate_settings(raw_settings):
    """Return cleaned settings using schemas collected from INSTALLED_APPS."""
    # Perform early validation on Django's INSTALLED_APPS.
    installed_apps = raw_settings['INSTALLED_APPS']
    schemas_mapping = raw_settings.get('CONFIT_SCHEMAS', {})
    # Create schema instance using INSTALLED_APPS.
    settings_schema = composite_schema(
        installed_apps=installed_apps,
        mapping=schemas_mapping)
    # Return cleaned settings.
    return settings_schema.deserialize(raw_settings)
