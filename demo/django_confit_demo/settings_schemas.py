"""Custom configuration schema(s)."""
import colander


class DjangoConfitDemoConfigurationSchema(colander.MappingSchema):
    CONFITDEMO_HELLO = colander.SchemaNode(
        colander.String(),
        missing=colander.required,
        default='',
    )
