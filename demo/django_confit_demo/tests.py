from django.conf import settings

import unittest


class TestSettings(unittest.TestCase):
    def test_settings(self):
        """Just make sure the settings are loaded."""
        # Default settings (Python module).
        self.assertTrue('django_nose' in settings.INSTALLED_APPS)
        # Local settings (JSON file).
        self.assertEqual(settings.SECRET_KEY, 'fake secret')
        # Test settings (YAML file).
        self.assertTrue('--tests=django_confit_demo' in settings.NOSE_ARGS)

    def test_custom_schema(self):
        """Custom DjangoConfitDemoConfigurationSchema was loaded."""
        self.assertEqual(settings.CONFITDEMO_HELLO, 'hello world!')
