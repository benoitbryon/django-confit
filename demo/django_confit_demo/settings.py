"""Django settings for `django-confit` demo project."""
import os

import django_confit


here = os.path.dirname(os.path.abspath(__file__))
etc_dir = os.path.join(os.path.dirname(here), 'etc')


# Load settings from various locations.
raw_settings = {}
raw_settings.update(django_confit.load_module(
    '{package}.default_settings'.format(package=__package__)))
raw_settings.update(django_confit.load_file(
    open(os.path.join(etc_dir, 'local_settings.json'))))
raw_settings.update(django_confit.load_file(
    open(os.path.join(etc_dir, 'test_settings.yaml'))))
raw_settings.update(django_confit.load_mapping(
    os.environ, prefix='DJANGO_CONFIT_DEMO__'))

# Validate and clean settings.
cleaned_settings = django_confit.validate_settings(raw_settings)

# Update globals, because that's the way Django uses
# DJANGO_SETTINGS_MODULE.
globals().update(cleaned_settings)
