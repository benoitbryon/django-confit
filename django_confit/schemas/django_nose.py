"""Configuration schema(s) for django-nose."""
import colander


class ConfigurationSchema(colander.MappingSchema):
    NOSE_ARGS = colander.SchemaNode(
        colander.Sequence(),
        missing=[],
        default=[],
        children=[colander.SchemaNode(colander.String())]
    )
    NOSE_PLUGINS = colander.SchemaNode(
        colander.Sequence(),
        missing=[],
        default=[],
        children=[colander.SchemaNode(colander.String())]
    )
