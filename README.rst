#############
django-confit
#############

``django-confit`` makes it easy to manage Django configuration:

* load settings from various locations: modules, files, environment;

* validate settings at runtime: do not run the server if configuration is
  broken;

* validate settings on demand: diagnose configuration issues;

* register configuration schemas for your third-party apps and libraries.


*******
Example
*******

Let's compute configuration from various locations in ``settings.py``:

.. code:: python

   import os

   from django_confit import DjangoConfigurationSchema
   from django_confit import settings_from_module
   from django_confit import settings_from_string_mapping


   class MyProjectConfigurationSchema(DjangoConfigurationSchema):
       pass  # Nothing specific to the project.


   # Read settings.
   raw_settings = {}
   raw_settings.update(settings_from_module('myproject.default_settings'))
   raw_settings.update(settings_from_string_mapping(os.environ, prefix='MYPROJECT_')

   # Clean settings.
   schema = MyProjectConfigurationSchema()
   cleaned_settings = schema.deserialize(raw_settings)

   # Update globals, since that's what Django expects.
   globals().update(cleaned_settings)


**********
Ressources
**********

* Documentation: 
* PyPI page: 
* Code repository: https://github.com/benoitbryon/django-confit
* Bugtracker: https://github.com/benoitbryon/django-confit/issues
* Continuous integration: https://travis-ci.org/benoitbryon/django-confit
* Roadmap: https://github.com/benoitbryon/django-confit/issues/milestones
