#############
django-confit
#############

`django-confit` eases Django configuration management.

**As a Django  user**, in order to configure a project:

* `django-confit` helps you load the settings wherever they are, whatever the
  format: Python modules, environment variables, JSON, YAML...

* `django-confit` validates the settings, i.e. it tells you if some directive
  is missing, has wrong format...

**As a Django library developer**, in order to help your application's users:

* you write configuration schemas for your application, using `django-confit`'s
  toolkit and conventions.

* `django-confit` helps you document your application's specific
  configuration.

**As a non Django user**, in order to deploy and run a Django-powered project:

* you write the configuration as you like, depending on your workflow and your
  provisioning toolkit. You know the project can load them using
  `django-confit`.

* you expect applications to validate the configuration before they actually
  use it, and report errors with a readable output.


*******
Example
*******

In a project's ``settings.py`` file, let's load configuration from various
locations, then validate it:

.. code-block:: python

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


**************
Project status
**************

Today, `django-confit` is a proof of concept:

* loading settings is nice and easy.

* validating configuration is easy... provided you have the schemas.

* creating configuration schemas is verbose. It uses `colander`_ which has nice
  features, but may not be the definitive option.

* generating documentation from schemas is not implemented.

**The main limitation is that schemas are mandatory.** If some configuration
directive is not registered in a schema, it will not be present in validation
output. It means that, if you install a new third-party Django application,
you need the configuration schema for this application, else its settings will
not pass validation. **So the most-wanted contribution is submitting
configuration schemas for third-party applications.**

Notice that this behaviour is a wanted feature. As `django-confit` author, I
think **libraries should always provide a schema for the settings they use**.
I do not pretend `django-confit` should be THE answer. I just bet that, if
schemas were widely adopted by the Django community, configuration would be
easier to manage.

`django-confit` does not pretend to be the ultimate configuration management
app for Django. Its goal is to show how some issues could be resolved, and to
highlight the benefits. `django-confit` is a proposal. If you like its
concepts, then you can:

* use `django-confit` of course!

* discuss, spread the word, send feedback.

* improve code. Help around configuration schemas of third-party apps would be
  appreciated.


**********
Ressources
**********

* Documentation: https://django-confit.readthedocs.org
* PyPI page: https://pypi.python.org/pypi/django-confit/
* Code repository: https://github.com/benoitbryon/django-confit
* Bugtracker: https://github.com/benoitbryon/django-confit/issues
* Continuous integration: https://travis-ci.org/benoitbryon/django-confit
* Roadmap: https://github.com/benoitbryon/django-confit/issues/milestones


.. _`colander`: https://pypi.python.org/pypi/colander/
