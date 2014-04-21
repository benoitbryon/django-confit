"""Default settings for `django-confit-demo`."""
INSTALLED_APPS = (
    'django_confit_demo',
    'django_nose',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
ROOT_URLCONF = '{package}.urls'.format(package=__package__)
WSGI_APPLICATION = '{package}.wsgi.application'.format(package=__package__)
