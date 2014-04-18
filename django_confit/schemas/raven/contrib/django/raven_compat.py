"""Configuration schema(s) for Raven."""
import colander


class ConfigurationSchema(colander.Schema):
    """Configuration for Raven, the official Sentry client."""
    RAVEN_CONFIG = colander.SchemaNode(
        colander.Mapping(unknown='raise'),
        missing=colander.required,
        default=colander.null,
        children=[
            colander.SchemaNode(
                colander.String(),
                name='dsn',
                missing=colander.required,
                default=colander.null,
            )
        ]
    )
    SENTRY_CLIENT = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='raven.contrib.django.raven_compat.DjangoClient',
    )
