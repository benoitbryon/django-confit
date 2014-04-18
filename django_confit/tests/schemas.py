"""Tests around django-confit schemas features."""
import unittest

import django_confit


class CompositeConfigurationSchemaTestCase(unittest.TestCase):
    def test_empty_installed_apps(self):
        """With empty INSTALLED_APPS, only Django schema is used."""
        raw_settings = {
            'DATABASES': {},
            'INSTALLED_APPS': [],
            'ROOT_URLCONF': 'fake.urls',
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
