"""Configuration schemas for the 1.6 branch."""
import django
from django.conf import global_settings

import colander

from django_confit.schemas.django_common import DjangoConfigurationSchema


if django.VERSION[0] == 1 and django.VERSION[1] == 6:

    class Django1_6ConfigurationSchema(DjangoConfigurationSchema):
        """Schema for Django 1.6 built-in settings."""
        #: New in Django 1.6
        CSRF_COOKIE_HTTPONLY = colander.SchemaNode(
            colander.Boolean(),
            missing=global_settings.CSRF_COOKIE_HTTPONLY,
            default=global_settings.CSRF_COOKIE_HTTPONLY,
        )
        #: Deprecated in Django 1.6.
        CACHE_MIDDLEWARE_ANONYMOUS_ONLY = colander.SchemaNode(
            colander.Boolean(),
            missing=colander.drop,  # Not in django.conf.global_settings.
            default=False,
        )
        # Deprecated in Django 1.6.
        SEND_BROKEN_LINK_EMAILS = colander.SchemaNode(
            colander.Boolean(),
            missing=global_settings.SEND_BROKEN_LINK_EMAILS,
            default=global_settings.SEND_BROKEN_LINK_EMAILS,
        )
        SESSION_SERIALIZER = colander.SchemaNode(
            colander.String(),
            missing=global_settings.SESSION_SERIALIZER,
            default=global_settings.SESSION_SERIALIZER,
        )

        def __init__(self, *args, **kwargs):
            """Overrides default config by adding new nodes only.
            """
            # init mapping
            super(Django1_6ConfigurationSchema, self).__init__(*args, **kwargs)

            # new nodes to add to db default config
            databases_default_nodes = [
                # New in Django 1.6.
                colander.SchemaNode(
                    colander.Boolean(),
                    name='ATOMIC_REQUESTS',
                    missing=colander.drop,
                    default=False,
                ),
                # New in Django 1.6.
                colander.SchemaNode(
                    colander.Boolean(),
                    name='AUTOCOMMIT',
                    missing=colander.drop,
                    default=True,
                ),
                # New in Django 1.6.
                colander.SchemaNode(
                    colander.Integer(),
                    name='CONN_MAX_AGE',
                    missing=colander.drop,
                    default=0,
                ),
            ]

            # shortcut to db default config to update
            databases_default = self.get('DATABASES').get('default')

            # add nodes
            for node in databases_default_nodes:
                databases_default.add(node)

    class Django1_6_1ConfigurationSchema(Django1_6ConfigurationSchema):
        pass

    class Django1_6_2ConfigurationSchema(Django1_6ConfigurationSchema):
        pass

    class Django1_6_3ConfigurationSchema(Django1_6ConfigurationSchema):
        pass

    class Django1_6_4ConfigurationSchema(Django1_6ConfigurationSchema):
        pass

    class Django1_6_5ConfigurationSchema(Django1_6ConfigurationSchema):
        pass
