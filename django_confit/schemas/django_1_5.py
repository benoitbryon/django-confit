"""Configuration schemas for the 1.5 branch."""
import django
from django.conf import global_settings

import colander

from django_confit.schemas.django_common import DjangoConfigurationSchema


if django.VERSION[0] == 1 and django.VERSION[1] == 5:

    class Django1_5ConfigurationSchema(DjangoConfigurationSchema):
        pass

    class Django1_5_1ConfigurationSchema(DjangoConfigurationSchema):
        pass

    class Django1_5_2ConfigurationSchema(DjangoConfigurationSchema):
        pass

    class Django1_5_3ConfigurationSchema(DjangoConfigurationSchema):

        SESSION_SERIALIZER = colander.SchemaNode(
            colander.String(),
            missing=global_settings.SESSION_SERIALIZER,
            default=global_settings.SESSION_SERIALIZER,
        )

    class Django1_5_4ConfigurationSchema(Django1_5_3ConfigurationSchema):
        pass

    class Django1_5_5ConfigurationSchema(Django1_5_3ConfigurationSchema):
        pass

    class Django1_5_6ConfigurationSchema(Django1_5_3ConfigurationSchema):
        pass

    class Django1_5_7ConfigurationSchema(Django1_5_3ConfigurationSchema):
        pass

    class Django1_5_8ConfigurationSchema(Django1_5_3ConfigurationSchema):
        pass
