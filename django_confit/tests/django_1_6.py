"""Unittests for the Django 1.5 branch."""
import unittest

import colander
import django

from django_confit import DjangoConfigurationSchema


@unittest.skipIf(
    django.VERSION[0] != 1 or django.VERSION[1] != 6,
    "Test for Django 1.6 only")
class Django1_6_ConfigurationSchemaTestCase(unittest.TestCase):
    def setUp(self):
        super(Django1_6_ConfigurationSchemaTestCase, self).setUp()
        #: Minimal valid Django settings.
        self.minimal_settings = {
            'DATABASES': {},
            'INSTALLED_APPS': [],
            'ROOT_URLCONF': 'fake.urls',
            'SECRET_KEY': '42',
        }

    def test_required(self):
        """Minimal settings for Django 1.6."""
        schema = DjangoConfigurationSchema()
        # Validate empty settings: invalid because some settings are required.
        raw_settings = {}
        with self.assertRaises(colander.Invalid):
            schema.deserialize(raw_settings)
        # Validate minimal settings: pass.
        cleaned_settings = schema.deserialize(self.minimal_settings)
        self.assertEqual(cleaned_settings['SECRET_KEY'], '42')
        self.assertEqual(cleaned_settings['INSTALLED_APPS'], [])
        self.assertEqual(cleaned_settings['DATABASES'], {'default': None})
        self.assertEqual(cleaned_settings['ROOT_URLCONF'], 'fake.urls')

    def test_template_loaders(self):
        """TEMPLATE_LOADERS accepts either strings or tuples."""
        schema = DjangoConfigurationSchema()
        # Just strings.
        raw_settings = self.minimal_settings
        raw_settings['TEMPLATE_LOADERS'] = [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]
        cleaned_settings = schema.deserialize(raw_settings)  # Is valid.
        self.assertEqual(cleaned_settings['TEMPLATE_LOADERS'],
                         raw_settings['TEMPLATE_LOADERS'])
        # Strings and tuples.
        raw_settings = self.minimal_settings
        raw_settings['TEMPLATE_LOADERS'] = [
            'some.string',
            (
                'django.template.loaders.cached.Loader',
                (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                )
            ),
        ]
        cleaned_settings = schema.deserialize(raw_settings)  # Is valid.
        self.assertEqual(cleaned_settings['TEMPLATE_LOADERS'],
                         raw_settings['TEMPLATE_LOADERS'])
