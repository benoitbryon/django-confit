#############
django-confit
#############

`django-confit` eases Django configuration management.

As a Django user:

* you write the settings as you like: Python modules, environment variables,
  JSON, YAML... `django-confit` helps you load them all.

* `django-confit` validates the settings, i.e. it tells you if some directive
  is missing, has wrong format...

As a Django application developer:

* you write configuration schemas for your application, using `django-confit`'s
  toolkit and conventions.

* `django-confit` helps you document your application's specific
  configuration.


*******
Example
*******

In a project's ``settings.py`` file, let's load configuration from various
locations then validate them:

.. code:: python

   import os

   import django_confit

   # Load settings.
   raw_settings = {}
   raw_settings.update(django_confit.load_module('myproject.default_settings'))
   raw_settings.update(django_confit.load_file(open('/etc/myproject.json')))
   raw_settings.update(django_confit.load_mapping(os.environ, prefix='MYPROJECT_')

   # Validate and clean settings.
   cleaned_settings = django_confit.validate_settings(raw_settings)

   # Update globals, because that's the way Django uses DJANGO_SETTINGS_MODULE.
   globals().update(cleaned_settings)


**********
Ressources
**********

* Documentation: https://django-confit.readthedocs.org
* PyPI page: https://pypi.python.org/pypi/django-confit/
* Code repository: https://github.com/benoitbryon/django-confit
* Bugtracker: https://github.com/benoitbryon/django-confit/issues
* Continuous integration: https://travis-ci.org/benoitbryon/django-confit
* Roadmap: https://github.com/benoitbryon/django-confit/issues/milestones
