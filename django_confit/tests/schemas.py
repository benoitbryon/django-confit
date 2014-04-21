"""Tests around django-confit schemas features."""
import difflib
import unittest

import django_confit


class CompositeConfigurationSchemaTestCase(unittest.TestCase):
    def test_empty_installed_apps(self):
        """With empty INSTALLED_APPS, only Django schema is used."""
        raw_settings = {
            'DATABASES': {},
            'INSTALLED_APPS': [],
            'SECRET_KEY': '42',
        }
        cleaned_settings = django_confit.validate_settings(raw_settings)
        self.assertEqual(cleaned_settings['SECRET_KEY'], '42')
        self.assertFalse('PIPELINE_CSS' in cleaned_settings)

    def test_pipeline_installed_apps(self):
        """With 'pipeline' in INSTALLED_APPS, 'pipeline' schema is added."""
        raw_settings = {
            'DATABASES': {},
            'INSTALLED_APPS': ['pipeline'],
            'ROOT_URLCONF': 'fake.urls',
            'SECRET_KEY': '42',
        }
        cleaned_settings = django_confit.validate_settings(raw_settings)
        self.assertEqual(cleaned_settings['SECRET_KEY'], '42')
        self.assertTrue('PIPELINE_CSS' in cleaned_settings)


class DjangoConfigurationSchemaTestCase(unittest.TestCase):
    def test_default_keys(self):
        """Django settings and DjangoConfigurationSchema have the same keys."""
        django_defaults = django_confit.load_module(
            'django.conf.global_settings')
        django_keys = list(django_defaults.keys())
        django_keys.sort()
        raw_settings = {  # Minimal settings for validation.
            'DATABASES': {},
            'INSTALLED_APPS': [],
            'SECRET_KEY': '42',
        }
        confit_defaults = django_confit.validate_settings(raw_settings)
        confit_keys = list(confit_defaults.keys())
        confit_keys.sort()
        diff = difflib.unified_diff(django_keys, confit_keys)
        self.assertEqual(
            django_keys,
            confit_keys,
            '\n'.join(diff))
