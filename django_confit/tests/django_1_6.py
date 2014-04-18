"""Unittests for the Django 1.5 branch."""
import unittest

import colander
import django

from django_confit import DjangoConfigurationSchema


@unittest.skipIf(
    django.VERSION[0] != 1 or django.VERSION[1] != 6,
    "Test for Django 1.6 only")
class Django1_6_ConfigurationSchemaTestCase(unittest.TestCase):
    def test_required(self):
        """Minimal settings for Django 1.6."""
        schema = DjangoConfigurationSchema()
        # Validate empty settings: invalid because some settings are required.
        raw_settings = {}
        with self.assertRaises(colander.Invalid):
            schema.deserialize(raw_settings)
        # Validate minimal settings: pass.
        raw_settings = {
            'DATABASES': {},
            'INSTALLED_APPS': [],
            'ROOT_URLCONF': 'fake.urls',
            'SECRET_KEY': '42',
        }
        cleaned_settings = schema.deserialize(raw_settings)
        self.assertEqual(cleaned_settings['SECRET_KEY'], '42')
