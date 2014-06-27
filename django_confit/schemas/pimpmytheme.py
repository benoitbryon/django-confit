"""Configuration schema for django-pimpmytheme."""
import colander


class ConfigurationSchema(colander.MappingSchema):
    """Configuration schema for django-pimpmytheme.

    Reference is https://github.com/novapost/django-pimpmytheme

    """
    CUSTOM_THEME_LOOKUP_OBJECT = colander.SchemaNode(
        colander.String(),
        missing='django.contrib.sites.models.Site',
        default='django.contrib.sites.models.Site',
    )
    CUSTOM_THEME_LOOKUP_ATTR = colander.SchemaNode(
        colander.String(),
        missing='name',
        default='name',
    )
    PIMPMYTHEME_FOLDER = colander.SchemaNode(
        colander.String(),
        missing=colander.required,
        default='',
    )
