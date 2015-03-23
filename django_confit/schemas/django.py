"""Configuration schemas for Django."""
from __future__ import absolute_import

import django
from django.conf import global_settings
from django.contrib import messages

import colander

from django_confit.utils.colander import TupleOrNone


class DjangoBaseConfigurationSchema(colander.MappingSchema):
    """Base schema for Django common settings.

    Currently based on Django version 1.5.

    Only settings that remain in all supported versions are listed here.
    Settings that have been updated or removed are managed in "migrations"
    (patches).

    This base class helps keeping as DRY as possible.

    """
    ABSOLUTE_URL_OVERRIDES = colander.SchemaNode(
        colander.Mapping(unknown='preserve'),
        missing=global_settings.ABSOLUTE_URL_OVERRIDES,
        default=global_settings.ABSOLUTE_URL_OVERRIDES,
    )
    ADMIN_FOR = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.ADMIN_FOR,
        default=global_settings.ADMIN_FOR,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    ADMINS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.ADMINS,
        default=global_settings.ADMINS,
        children=[
            colander.SchemaNode(
                colander.Tuple(),
                children=[
                    colander.SchemaNode(colander.String()),
                    colander.SchemaNode(
                        colander.String(),
                        validator=colander.Email(),
                    ),
                ]
            ),
        ]
    )
    ALLOWED_HOSTS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.ALLOWED_HOSTS,
        default=global_settings.ALLOWED_HOSTS,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    ALLOWED_INCLUDE_ROOTS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.ALLOWED_INCLUDE_ROOTS,
        default=global_settings.ALLOWED_INCLUDE_ROOTS,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    APPEND_SLASH = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.APPEND_SLASH,
        default=global_settings.APPEND_SLASH,
    )
    AUTHENTICATION_BACKENDS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.AUTHENTICATION_BACKENDS,
        default=global_settings.AUTHENTICATION_BACKENDS,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    AUTH_USER_MODEL = colander.SchemaNode(
        colander.String(),
        missing=global_settings.AUTH_USER_MODEL,
        default=global_settings.AUTH_USER_MODEL,
    )
    CACHES = colander.SchemaNode(
        colander.Mapping(unknown='preserve'),
        missing=global_settings.CACHES,
        default=global_settings.CACHES,
        children=[
            colander.SchemaNode(
                colander.Mapping(unknown='raise'),
                name='default',
                missing=colander.drop,
                children=[
                    colander.SchemaNode(
                        colander.String(),
                        name='BACKEND',
                        missing=colander.required,
                        default=colander.null,
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='KEY_FUNCTION',
                        missing=colander.drop,
                        default='',
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='KEY_PREFIX',
                        missing=colander.drop,
                        default='',
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='LOCATION',
                        missing=colander.drop,
                        default='',
                    ),
                    colander.SchemaNode(
                        colander.Mapping(unknown='preserve'),
                        name='OPTIONS',
                        missing=colander.drop,
                        default={},
                    ),
                    colander.SchemaNode(
                        colander.Integer(),
                        name='TIMEOUT',
                        missing=colander.drop,
                        default=300,
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='VERSION',
                        missing=colander.drop,
                        default=1,
                    ),
                ]
            ),
        ]
    )
    CACHE_MIDDLEWARE_ALIAS = colander.SchemaNode(
        colander.String(),
        missing=global_settings.CACHE_MIDDLEWARE_ALIAS,
        default=global_settings.CACHE_MIDDLEWARE_ALIAS,
    )
    CACHE_MIDDLEWARE_ANONYMOUS_ONLY = colander.SchemaNode(
        colander.Boolean(),
        missing=colander.drop,  # Not in django.conf.global_settings.
        default=False,
    )
    CACHE_MIDDLEWARE_KEY_PREFIX = colander.SchemaNode(
        colander.String(),
        missing=global_settings.CACHE_MIDDLEWARE_KEY_PREFIX,
        default=global_settings.CACHE_MIDDLEWARE_KEY_PREFIX,
    )
    CACHE_MIDDLEWARE_SECONDS = colander.SchemaNode(
        colander.Integer(),
        missing=global_settings.CACHE_MIDDLEWARE_SECONDS,
        default=global_settings.CACHE_MIDDLEWARE_SECONDS,
    )
    COMMENTS_ALLOW_PROFANITIES = colander.SchemaNode(
        colander.Boolean(),
        missing=False,
        default=False,
    )
    CSRF_COOKIE_DOMAIN = colander.SchemaNode(
        colander.String(),
        missing=global_settings.CSRF_COOKIE_DOMAIN,
        default=global_settings.CSRF_COOKIE_DOMAIN,
    )
    CSRF_COOKIE_NAME = colander.SchemaNode(
        colander.String(),
        missing=global_settings.CSRF_COOKIE_NAME,
        default=global_settings.CSRF_COOKIE_NAME,
    )
    CSRF_COOKIE_PATH = colander.SchemaNode(
        colander.String(),
        missing=global_settings.CSRF_COOKIE_PATH,
        default=global_settings.CSRF_COOKIE_PATH,
    )
    CSRF_COOKIE_SECURE = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.CSRF_COOKIE_SECURE,
        default=global_settings.CSRF_COOKIE_SECURE,
    )
    CSRF_FAILURE_VIEW = colander.SchemaNode(
        colander.String(),
        missing=global_settings.CSRF_FAILURE_VIEW,
        default=global_settings.CSRF_FAILURE_VIEW,
    )
    DATABASES = colander.SchemaNode(
        colander.Mapping(unknown='preserve'),
        missing=colander.required,
        default=colander.null,
        children=[
            colander.SchemaNode(
                colander.Mapping(unknown='raise'),
                name='default',
                missing=None,
                children=[
                    # See django.db.utils.ConnectionHandler.ensure_defaults
                    colander.SchemaNode(
                        colander.String(),
                        name='ENGINE',
                        missing=colander.drop,
                        default='',
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='HOST',
                        missing=colander.drop,
                        default='',
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='NAME',
                        missing=colander.drop,
                        default='',
                    ),
                    colander.SchemaNode(
                        colander.Mapping(unknown='preserve'),
                        name='OPTIONS',
                        missing=colander.drop,
                        default={},
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='PASSWORD',
                        missing=colander.drop,
                        default='',
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='PORT',
                        missing=colander.drop,
                        default='',
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='USER',
                        missing=colander.drop,
                        default='',
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='TEST_CHARSET',
                        missing=colander.drop,
                        default=None,
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='TEST_COLLATION',
                        missing=colander.drop,
                        default=None,
                    ),
                    colander.SchemaNode(
                        colander.Sequence(),
                        name='TEST_DEPENDENCIES',
                        missing=colander.drop,
                        default=['default'],
                        children=[
                            colander.SchemaNode(colander.String()),
                        ]
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='TEST_MIRROR',
                        missing=colander.drop,
                        default=None,
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='TEST_NAME',
                        missing=colander.drop,
                        default=None,
                    ),
                    colander.SchemaNode(
                        colander.Boolean(),
                        name='TEST_CREATE',
                        missing=colander.drop,
                        default=True,
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='TEST_USER',
                        missing=colander.drop,
                        default=None,
                    ),
                    colander.SchemaNode(
                        colander.Boolean(),
                        name='TEST_USER_CREATE',
                        missing=colander.drop,
                        default=True,
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='TEST_PASSWD',
                        missing=colander.drop,
                        default=None,
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='TEST_TBLSPACE',
                        missing=colander.drop,
                        default=None,
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='TEST_TBLSPACE_TMP',
                        missing=colander.drop,
                        default=None,
                    ),
                ]
            ),
        ]
    )
    DATABASE_ROUTERS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.DATABASE_ROUTERS,
        default=global_settings.DATABASE_ROUTERS,
        children=[
            colander.SchemaNode(
                colander.String(),
            ),
        ]
    )
    DATE_FORMAT = colander.SchemaNode(
        colander.String(),
        missing=global_settings.DATE_FORMAT,
        default=global_settings.DATE_FORMAT,
    )
    DATE_INPUT_FORMATS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.DATE_INPUT_FORMATS,
        default=global_settings.DATE_INPUT_FORMATS,
        children=[
            colander.SchemaNode(
                colander.String(),
            ),
        ]
    )
    DATETIME_FORMAT = colander.SchemaNode(
        colander.String(),
        missing=global_settings.DATETIME_FORMAT,
        default=global_settings.DATETIME_FORMAT,
    )
    DATETIME_INPUT_FORMATS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.DATETIME_INPUT_FORMATS,
        default=global_settings.DATETIME_INPUT_FORMATS,
        children=[
            colander.SchemaNode(
                colander.String(),
            ),
        ]
    )
    DEBUG = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.DEBUG,
        default=global_settings.DEBUG,
    )
    DEBUG_PROPAGATE_EXCEPTIONS = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.DEBUG,
        default=global_settings.DEBUG,
    )
    DECIMAL_SEPARATOR = colander.SchemaNode(
        colander.String(),
        missing=global_settings.DECIMAL_SEPARATOR,
        default=global_settings.DECIMAL_SEPARATOR,
    )
    DEFAULT_CHARSET = colander.SchemaNode(
        colander.String(),
        missing=global_settings.DEFAULT_CHARSET,
        default=global_settings.DEFAULT_CHARSET,
    )
    DEFAULT_CONTENT_TYPE = colander.SchemaNode(
        colander.String(),
        missing=global_settings.DEFAULT_CONTENT_TYPE,
        default=global_settings.DEFAULT_CONTENT_TYPE,
    )
    DEFAULT_EXCEPTION_REPORTER_FILTER = colander.SchemaNode(
        colander.String(),
        missing=global_settings.DEFAULT_EXCEPTION_REPORTER_FILTER,
        default=global_settings.DEFAULT_EXCEPTION_REPORTER_FILTER,
    )
    DEFAULT_FILE_STORAGE = colander.SchemaNode(
        colander.String(),
        missing=global_settings.DEFAULT_FILE_STORAGE,
        default=global_settings.DEFAULT_FILE_STORAGE,
    )
    DEFAULT_FROM_EMAIL = colander.SchemaNode(
        colander.String(),
        missing=global_settings.DEFAULT_FROM_EMAIL,
        default=global_settings.DEFAULT_FROM_EMAIL,
        validator=colander.Email(),
    )
    DEFAULT_INDEX_TABLESPACE = colander.SchemaNode(
        colander.String(),
        missing=global_settings.DEFAULT_INDEX_TABLESPACE,
        default=global_settings.DEFAULT_INDEX_TABLESPACE,
    )
    DEFAULT_TABLESPACE = colander.SchemaNode(
        colander.String(),
        missing=global_settings.DEFAULT_TABLESPACE,
        default=global_settings.DEFAULT_TABLESPACE,
    )
    DISALLOWED_USER_AGENTS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.DISALLOWED_USER_AGENTS,
        default=global_settings.DISALLOWED_USER_AGENTS,
        children=[
            colander.SchemaNode(
                colander.String(),
            ),
        ]
    )
    EMAIL_BACKEND = colander.SchemaNode(
        colander.String(),
        missing=global_settings.EMAIL_BACKEND,
        default=global_settings.EMAIL_BACKEND,
    )
    EMAIL_FILE_PATH = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,  # Not in djanco.conf.globalsettings
        default=colander.null,
    )
    EMAIL_HOST = colander.SchemaNode(
        colander.String(),
        missing=global_settings.EMAIL_HOST,
        default=global_settings.EMAIL_HOST,
    )
    EMAIL_HOST_PASSWORD = colander.SchemaNode(
        colander.String(),
        missing=global_settings.EMAIL_HOST_PASSWORD,
        default=global_settings.EMAIL_HOST_PASSWORD,
    )
    EMAIL_HOST_USER = colander.SchemaNode(
        colander.String(),
        missing=global_settings.EMAIL_HOST_USER,
        default=global_settings.EMAIL_HOST_USER,
    )
    EMAIL_PORT = colander.SchemaNode(
        colander.Integer(),
        missing=global_settings.EMAIL_PORT,
        default=global_settings.EMAIL_PORT,
    )
    EMAIL_SUBJECT_PREFIX = colander.SchemaNode(
        colander.String(),
        missing=global_settings.EMAIL_SUBJECT_PREFIX,
        default=global_settings.EMAIL_SUBJECT_PREFIX,
    )
    EMAIL_USE_TLS = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.EMAIL_USE_TLS,
        default=global_settings.EMAIL_USE_TLS,
    )
    FORMAT_MODULE_PATH = colander.SchemaNode(
        colander.String(),
        missing=global_settings.FORMAT_MODULE_PATH,
        default=global_settings.FORMAT_MODULE_PATH,
    )
    FILE_CHARSET = colander.SchemaNode(
        colander.String(),
        missing=global_settings.FILE_CHARSET,
        default=global_settings.FILE_CHARSET,
    )
    FILE_UPLOAD_HANDLERS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.FILE_UPLOAD_HANDLERS,
        default=global_settings.FILE_UPLOAD_HANDLERS,
        children=[
            colander.SchemaNode(
                colander.String(),
            ),
        ]
    )
    FILE_UPLOAD_MAX_MEMORY_SIZE = colander.SchemaNode(
        colander.Integer(),
        missing=global_settings.FILE_UPLOAD_MAX_MEMORY_SIZE,
        default=global_settings.FILE_UPLOAD_MAX_MEMORY_SIZE,
    )
    FILE_UPLOAD_PERMISSIONS = colander.SchemaNode(
        colander.Integer(),
        missing=global_settings.FILE_UPLOAD_PERMISSIONS,
        default=global_settings.FILE_UPLOAD_PERMISSIONS,
    )
    FILE_UPLOAD_TEMP_DIR = colander.SchemaNode(
        colander.String(),
        missing=global_settings.FILE_UPLOAD_TEMP_DIR,
        default=global_settings.FILE_UPLOAD_TEMP_DIR,
    )
    FIRST_DAY_OF_WEEK = colander.SchemaNode(
        colander.Integer(),
        missing=global_settings.FIRST_DAY_OF_WEEK,
        default=global_settings.FIRST_DAY_OF_WEEK,
    )
    FIXTURE_DIRS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.FIXTURE_DIRS,
        default=global_settings.FIXTURE_DIRS,
        children=[
            colander.SchemaNode(
                colander.String(),
            ),
        ]
    )
    FORCE_SCRIPT_NAME = colander.SchemaNode(
        colander.String(),
        missing=global_settings.FORCE_SCRIPT_NAME,
        default=global_settings.FORCE_SCRIPT_NAME,
    )
    IGNORABLE_404_URLS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.IGNORABLE_404_URLS,
        default=global_settings.IGNORABLE_404_URLS,
        children=[
            colander.SchemaNode(
                colander.String(),
            ),
        ]
    )
    INSTALLED_APPS = colander.SchemaNode(
        colander.Sequence(),
        missing=colander.required,
        default=colander.null,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    INTERNAL_IPS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.INTERNAL_IPS,
        default=global_settings.INTERNAL_IPS,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    LANGUAGE_CODE = colander.SchemaNode(
        colander.String(),
        missing=global_settings.LANGUAGE_CODE,
        default=global_settings.LANGUAGE_CODE,
    )
    LANGUAGE_COOKIE_NAME = colander.SchemaNode(
        colander.String(),
        missing=global_settings.LANGUAGE_COOKIE_NAME,
        default=global_settings.LANGUAGE_COOKIE_NAME,
    )
    LANGUAGES = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.LANGUAGES,
        default=global_settings.LANGUAGES,
        children=[
            colander.SchemaNode(
                colander.Tuple(),
                children=[
                    colander.SchemaNode(colander.String()),
                    colander.SchemaNode(colander.String()),
                ]
            ),
        ]
    )
    LANGUAGES_BIDI = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.LANGUAGES_BIDI,
        default=global_settings.LANGUAGES_BIDI,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    LOCALE_PATHS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.LOCALE_PATHS,
        default=global_settings.LOCALE_PATHS,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    LOGGING = colander.SchemaNode(
        colander.Mapping(unknown='preserve'),
        missing=global_settings.LOGGING,
        default=global_settings.LOGGING,
    )
    LOGGING_CONFIG = colander.SchemaNode(
        colander.String(),
        missing=global_settings.LOGGING_CONFIG,
        default=global_settings.LOGGING_CONFIG,
    )
    LOGIN_REDIRECT_URL = colander.SchemaNode(
        colander.String(),
        missing=global_settings.LOGIN_REDIRECT_URL,
        default=global_settings.LOGIN_REDIRECT_URL,
    )
    LOGIN_URL = colander.SchemaNode(
        colander.String(),
        missing=global_settings.LOGIN_URL,
        default=global_settings.LOGIN_URL,
    )
    LOGOUT_URL = colander.SchemaNode(
        colander.String(),
        missing=global_settings.LOGOUT_URL,
        default=global_settings.LOGOUT_URL,
    )
    MANAGERS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.MANAGERS,
        default=global_settings.MANAGERS,
        children=[
            colander.SchemaNode(
                colander.Tuple(),
                children=[
                    colander.SchemaNode(colander.String()),
                    colander.SchemaNode(
                        colander.String(),
                        validator=colander.Email(),
                    ),
                ]
            ),
        ]
    )
    MEDIA_ROOT = colander.SchemaNode(
        colander.String(),
        missing=global_settings.MEDIA_ROOT,
        default=global_settings.MEDIA_ROOT,
    )
    MEDIA_URL = colander.SchemaNode(
        colander.String(),
        missing=global_settings.MEDIA_URL,
        default=global_settings.MEDIA_URL,
    )
    MESSAGE_LEVEL = colander.SchemaNode(
        colander.Integer(),
        missing=colander.drop,  # Not in django.conf.global_settings
        default=messages.INFO,
    )
    MESSAGE_STORAGE = colander.SchemaNode(
        colander.String(),
        missing=global_settings.MESSAGE_STORAGE,
        default=global_settings.MESSAGE_STORAGE,
    )
    MESSAGE_TAGS = colander.SchemaNode(
        colander.Mapping(unknown='preserve'),
        missing=colander.drop,  # Not in django.conf.global_settings
        default=messages.DEFAULT_TAGS,
        children=[
            colander.SchemaNode(
                colander.String(),
            ),
        ]
    )
    MIDDLEWARE_CLASSES = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.MIDDLEWARE_CLASSES,
        default=global_settings.MIDDLEWARE_CLASSES,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    MONTH_DAY_FORMAT = colander.SchemaNode(
        colander.String(),
        missing=global_settings.MONTH_DAY_FORMAT,
        default=global_settings.MONTH_DAY_FORMAT,
    )
    NUMBER_GROUPING = colander.SchemaNode(
        colander.Integer(),
        missing=global_settings.NUMBER_GROUPING,
        default=global_settings.NUMBER_GROUPING,
    )
    PASSWORD_HASHERS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.PASSWORD_HASHERS,
        default=global_settings.PASSWORD_HASHERS,
        children=[
            colander.SchemaNode(
                colander.String(),
            ),
        ]
    )
    PASSWORD_RESET_TIMEOUT_DAYS = colander.SchemaNode(
        colander.Integer(),
        missing=global_settings.PASSWORD_RESET_TIMEOUT_DAYS,
        default=global_settings.PASSWORD_RESET_TIMEOUT_DAYS,
    )
    PREPEND_WWW = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.PREPEND_WWW,
        default=global_settings.PREPEND_WWW,
    )
    PROFANITIES_LIST = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.PROFANITIES_LIST,
        default=global_settings.PROFANITIES_LIST,
        children=[
            colander.SchemaNode(
                colander.String(),
            ),
        ]
    )
    RESTRUCTUREDTEXT_FILTER_SETTINGS = colander.SchemaNode(
        colander.Mapping(unknown='preserve'),
        missing=colander.drop,  # Not in django.conf.global_settings
        default={},
    )
    ROOT_URLCONF = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,  # Not in django.conf.global_settings
        default=colander.null,
    )
    SECRET_KEY = colander.SchemaNode(
        colander.String(),
        missing=colander.required,
        default=colander.null,
    )
    SECURE_PROXY_SSL_HEADER = colander.SchemaNode(
        TupleOrNone(),
        missing=global_settings.SECURE_PROXY_SSL_HEADER,
        default=global_settings.SECURE_PROXY_SSL_HEADER,
        children=[
            colander.SchemaNode(colander.String()),
            colander.SchemaNode(colander.String()),
        ]
    )
    SEND_BROKEN_LINK_EMAILS = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.SEND_BROKEN_LINK_EMAILS,
        default=global_settings.SEND_BROKEN_LINK_EMAILS,
    )
    SERIALIZATION_MODULES = colander.SchemaNode(
        colander.Mapping(unknown='preserve'),
        missing=colander.drop,
        default={},
        children=[
            colander.SchemaNode(
                colander.String(),
            ),
        ]
    )
    SERVER_EMAIL = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SERVER_EMAIL,
        default=global_settings.SERVER_EMAIL,
    )
    SESSION_COOKIE_AGE = colander.SchemaNode(
        colander.Integer(),
        missing=global_settings.SESSION_COOKIE_AGE,
        default=global_settings.SESSION_COOKIE_AGE,
    )
    SESSION_COOKIE_DOMAIN = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SESSION_COOKIE_DOMAIN,
        default=global_settings.SESSION_COOKIE_DOMAIN,
    )
    SESSION_COOKIE_HTTPONLY = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.SESSION_COOKIE_HTTPONLY,
        default=global_settings.SESSION_COOKIE_HTTPONLY,
    )
    SESSION_COOKIE_NAME = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SESSION_COOKIE_NAME,
        default=global_settings.SESSION_COOKIE_NAME,
    )
    SESSION_COOKIE_PATH = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SESSION_COOKIE_PATH,
        default=global_settings.SESSION_COOKIE_PATH,
    )
    SESSION_CACHE_ALIAS = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SESSION_CACHE_ALIAS,
        default=global_settings.SESSION_CACHE_ALIAS,
    )
    SESSION_COOKIE_SECURE = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.SESSION_COOKIE_SECURE,
        default=global_settings.SESSION_COOKIE_SECURE,
    )
    SESSION_ENGINE = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SESSION_ENGINE,
        default=global_settings.SESSION_ENGINE,
    )
    SESSION_EXPIRE_AT_BROWSER_CLOSE = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.SESSION_EXPIRE_AT_BROWSER_CLOSE,
        default=global_settings.SESSION_EXPIRE_AT_BROWSER_CLOSE,
    )
    SESSION_FILE_PATH = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SESSION_FILE_PATH,
        default=global_settings.SESSION_FILE_PATH,
    )
    SESSION_SAVE_EVERY_REQUEST = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.SESSION_SAVE_EVERY_REQUEST,
        default=global_settings.SESSION_SAVE_EVERY_REQUEST,
    )
    SESSION_SERIALIZER = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SESSION_SERIALIZER,
        default=global_settings.SESSION_SERIALIZER,
    )
    SHORT_DATE_FORMAT = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SHORT_DATE_FORMAT,
        default=global_settings.SHORT_DATE_FORMAT,
    )
    SHORT_DATETIME_FORMAT = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SHORT_DATETIME_FORMAT,
        default=global_settings.SHORT_DATETIME_FORMAT,
    )
    SIGNING_BACKEND = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SIGNING_BACKEND,
        default=global_settings.SIGNING_BACKEND,
    )
    SITE_ID = colander.SchemaNode(
        colander.Integer(),
        missing=colander.drop,
        default=colander.null,
    )
    STATIC_ROOT = colander.SchemaNode(
        colander.String(),
        missing=global_settings.STATIC_ROOT,
        default=global_settings.STATIC_ROOT,
    )
    STATIC_URL = colander.SchemaNode(
        colander.String(),
        missing=global_settings.STATIC_URL,
        default=global_settings.STATIC_URL,
    )
    STATICFILES_DIRS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.STATICFILES_DIRS,
        default=global_settings.STATICFILES_DIRS,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    STATICFILES_FINDERS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.STATICFILES_FINDERS,
        default=global_settings.STATICFILES_FINDERS,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    STATICFILES_STORAGE = colander.SchemaNode(
        colander.String(),
        missing=global_settings.STATICFILES_STORAGE,
        default=global_settings.STATICFILES_STORAGE,
    )
    TEMPLATE_CONTEXT_PROCESSORS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.TEMPLATE_CONTEXT_PROCESSORS,
        default=global_settings.TEMPLATE_CONTEXT_PROCESSORS,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    TEMPLATE_DEBUG = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.TEMPLATE_DEBUG,
        default=global_settings.TEMPLATE_DEBUG,
    )
    TEMPLATE_DIRS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.TEMPLATE_DIRS,
        default=global_settings.TEMPLATE_DIRS,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    TEMPLATE_LOADERS = colander.SchemaNode(
        colander.List(),
        missing=global_settings.TEMPLATE_LOADERS,
        default=global_settings.TEMPLATE_LOADERS,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    TEMPLATE_STRING_IF_INVALID = colander.SchemaNode(
        colander.String(),
        missing=global_settings.TEMPLATE_STRING_IF_INVALID,
        default=global_settings.TEMPLATE_STRING_IF_INVALID,
    )
    TEST_RUNNER = colander.SchemaNode(
        colander.String(),
        missing=global_settings.TEST_RUNNER,
        default=global_settings.TEST_RUNNER,
    )
    THOUSAND_SEPARATOR = colander.SchemaNode(
        colander.String(),
        missing=global_settings.THOUSAND_SEPARATOR,
        default=global_settings.THOUSAND_SEPARATOR,
    )
    TIME_FORMAT = colander.SchemaNode(
        colander.String(),
        missing=global_settings.TIME_FORMAT,
        default=global_settings.TIME_FORMAT,
    )
    TIME_INPUT_FORMATS = colander.SchemaNode(
        colander.Sequence(),
        missing=global_settings.TIME_INPUT_FORMATS,
        default=global_settings.TIME_INPUT_FORMATS,
        children=[
            colander.SchemaNode(colander.String()),
        ]
    )
    TIME_ZONE = colander.SchemaNode(
        colander.String(),
        missing=global_settings.TIME_ZONE,
        default=global_settings.TIME_ZONE,
    )
    TRANSACTIONS_MANAGED = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.TRANSACTIONS_MANAGED,
        default=global_settings.TRANSACTIONS_MANAGED,
    )
    USE_ETAGS = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.USE_ETAGS,
        default=global_settings.USE_ETAGS,
    )
    USE_I18N = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.USE_I18N,
        default=global_settings.USE_I18N,
    )
    USE_L10N = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.USE_L10N,
        default=global_settings.USE_L10N,
    )
    USE_THOUSAND_SEPARATOR = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.USE_THOUSAND_SEPARATOR,
        default=global_settings.USE_THOUSAND_SEPARATOR,
    )
    USE_TZ = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.USE_TZ,
        default=global_settings.USE_TZ,
    )
    USE_X_FORWARDED_HOST = colander.SchemaNode(
        colander.Boolean(),
        missing=global_settings.USE_X_FORWARDED_HOST,
        default=global_settings.USE_X_FORWARDED_HOST,
    )
    WSGI_APPLICATION = colander.SchemaNode(
        colander.String(),
        missing=global_settings.WSGI_APPLICATION,
        default=global_settings.WSGI_APPLICATION,
    )
    YEAR_MONTH_FORMAT = colander.SchemaNode(
        colander.String(),
        missing=global_settings.YEAR_MONTH_FORMAT,
        default=global_settings.YEAR_MONTH_FORMAT,
    )
    X_FRAME_OPTIONS = colander.SchemaNode(
        colander.String(),
        missing=global_settings.X_FRAME_OPTIONS,
        default=global_settings.X_FRAME_OPTIONS,
    )


class Django1_5ConfigurationSchema(DjangoBaseConfigurationSchema):
    """Configuration schema for Django 1.5."""


class Django1_5_1ConfigurationSchema(Django1_5ConfigurationSchema):
    """Configuration schema for Django 1.5.1."""


class Django1_5_2ConfigurationSchema(Django1_5_1ConfigurationSchema):
    """Configuration schema for Django 1.5.2."""


class Django1_5_3ConfigurationSchema(Django1_5_2ConfigurationSchema):
    """Configuration schema for Django 1.5.3."""
    SESSION_SERIALIZER = colander.SchemaNode(
        colander.String(),
        missing=global_settings.SESSION_SERIALIZER,
        default=global_settings.SESSION_SERIALIZER,
    )


class Django1_5_4ConfigurationSchema(Django1_5_3ConfigurationSchema):
    """Configuration schema for Django 1.5.4."""


class Django1_5_5ConfigurationSchema(Django1_5_4ConfigurationSchema):
    """Configuration schema for Django 1.5.5."""


class Django1_5_6ConfigurationSchema(Django1_5_5ConfigurationSchema):
    """Configuration schema for Django 1.5.6."""
    pass


class Django1_5_7ConfigurationSchema(Django1_5_6ConfigurationSchema):
    """Configuration schema for Django 1.5.7."""
    pass


class Django1_5_8ConfigurationSchema(Django1_5_7ConfigurationSchema):
    """Configuration schema for Django 1.5.8."""
    pass


class Django1_5_9ConfigurationSchema(Django1_5_8ConfigurationSchema):
    """Configuration schema for Django 1.5.9."""
    pass


class Django1_5_10ConfigurationSchema(Django1_5_9ConfigurationSchema):
    """Configuration schema for Django 1.5.10."""
    pass


class Django1_5_11ConfigurationSchema(Django1_5_10ConfigurationSchema):
    """Configuration schema for Django 1.5.11."""
    pass


class Django1_5_12ConfigurationSchema(Django1_5_11ConfigurationSchema):
    """Configuration schema for Django 1.5.12."""
    pass


if django.VERSION[0] == 1 and django.VERSION[1] == 6:
    # Some default values taken from ``global_settings`` are not available in
    # Django 1.5, so we cannot run the code below in versions lower than 1.6.
    class Django1_6ConfigurationSchema(Django1_5_5ConfigurationSchema):
        """Configuration schema for Django 1.6."""
        CSRF_COOKIE_HTTPONLY = colander.SchemaNode(
            colander.Boolean(),
            missing=global_settings.CSRF_COOKIE_HTTPONLY,
            default=global_settings.CSRF_COOKIE_HTTPONLY,
        )
        CACHE_MIDDLEWARE_ANONYMOUS_ONLY = colander.SchemaNode(
            colander.Boolean(),
            missing=colander.drop,  # Not in django.conf.global_settings.
            default=False,
        )
        SEND_BROKEN_LINK_EMAILS = colander.SchemaNode(
            colander.Boolean(),
            missing=global_settings.SEND_BROKEN_LINK_EMAILS,
            default=global_settings.SEND_BROKEN_LINK_EMAILS,
        )

        def __init__(self, *args, **kwargs):
            """Overrides default config by adding new nodes only."""
            # Inherit from base schema.
            super(Django1_6ConfigurationSchema, self).__init__(*args, **kwargs)

            # Migrate from previous version.

            # New nodes to add to db default config.
            databases_default_nodes = [
                colander.SchemaNode(
                    colander.Boolean(),
                    name='ATOMIC_REQUESTS',
                    missing=colander.drop,
                    default=False,
                ),
                colander.SchemaNode(
                    colander.Boolean(),
                    name='AUTOCOMMIT',
                    missing=colander.drop,
                    default=True,
                ),
                colander.SchemaNode(
                    colander.Integer(),
                    name='CONN_MAX_AGE',
                    missing=colander.drop,
                    default=0,
                ),
            ]

            # Shortcut to db default config to update
            databases_default = self.get('DATABASES').get('default')

            # Add nodes
            for node in databases_default_nodes:
                databases_default.add(node)

    class Django1_6_1ConfigurationSchema(Django1_6ConfigurationSchema):
        """Configuration schema for Django 1.6.1."""

    class Django1_6_2ConfigurationSchema(Django1_6_1ConfigurationSchema):
        """Configuration schema for Django 1.6.2."""

    class Django1_6_3ConfigurationSchema(Django1_6_2ConfigurationSchema):
        """Configuration schema for Django 1.6.3."""

    class Django1_6_4ConfigurationSchema(Django1_6_3ConfigurationSchema):
        """Configuration schema for Django 1.6.4."""

    class Django1_6_5ConfigurationSchema(Django1_6_4ConfigurationSchema):
        """Configuration schema for Django 1.6.5."""

    class Django1_6_6ConfigurationSchema(Django1_6_5ConfigurationSchema):
        """Configuration schema for Django 1.6.6."""

    class Django1_6_7ConfigurationSchema(Django1_6_6ConfigurationSchema):
        """Configuration schema for Django 1.6.7."""

    class Django1_6_8ConfigurationSchema(Django1_6_7ConfigurationSchema):
        """Configuration schema for Django 1.6.8."""

    class Django1_6_9ConfigurationSchema(Django1_6_8ConfigurationSchema):
        """Configuration schema for Django 1.6.9."""

    class Django1_6_10ConfigurationSchema(Django1_6_9ConfigurationSchema):
        """Configuration schema for Django 1.6.10."""

    class Django1_6_11ConfigurationSchema(Django1_6_10ConfigurationSchema):
        """Configuration schema for Django 1.6.11."""
