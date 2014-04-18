"""Schemas for configuration validation."""
import django

from django_confit.utils.importlib import import_member


def get_current_schema_class():
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


DjangoConfigurationSchema = get_current_schema_class()
