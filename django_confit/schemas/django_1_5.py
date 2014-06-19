"""Configuration schemas for the 1.5 branch."""
import django

from django_confit.schemas.django_x import DjangoConfigurationSchema


if django.VERSION[0] == 1 and django.VERSION[1] == 5:

    class Django1_5ConfigurationSchema(DjangoConfigurationSchema):
        pass

    class Django1_5_1ConfigurationSchema(DjangoConfigurationSchema):
        pass

    class Django1_5_2ConfigurationSchema(DjangoConfigurationSchema):
        pass

    class Django1_5_3ConfigurationSchema(DjangoConfigurationSchema):
        pass

    class Django1_5_4ConfigurationSchema(DjangoConfigurationSchema):
        pass

    class Django1_5_5ConfigurationSchema(DjangoConfigurationSchema):
        pass

    class Django1_5_6ConfigurationSchema(DjangoConfigurationSchema):
        pass

    class Django1_5_7ConfigurationSchema(DjangoConfigurationSchema):
        pass

    class Django1_5_8ConfigurationSchema(DjangoConfigurationSchema):
        pass
