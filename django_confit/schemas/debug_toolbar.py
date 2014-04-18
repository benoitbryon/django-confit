"""Configuration schema(s) for django-debug-toolbar."""
import colander


class ConfigurationSchema(colander.MappingSchema):
    DEBUG_TOOLBAR_CONFIG = colander.SchemaNode(
        colander.Mapping(unknown='preserve')
    )
    DEBUG_TOOLBAR_PATCH_SETTINGS = colander.SchemaNode(
        colander.Boolean(),
        missing=colander.drop,
        default=False,
    )
    DEBUG_TOOLBAR_PANELS = colander.SchemaNode(
        colander.Sequence(),
        missing=colander.drop,
        default=[
            'debug_toolbar.panels.versions.VersionsPanel',
            'debug_toolbar.panels.timer.TimerPanel',
            'debug_toolbar.panels.settings.SettingsPanel',
            'debug_toolbar.panels.headers.HeadersPanel',
            'debug_toolbar.panels.request.RequestPanel',
            'debug_toolbar.panels.sql.SQLPanel',
            'debug_toolbar.panels.staticfiles.StaticFilesPanel',
            'debug_toolbar.panels.templates.TemplatesPanel',
            'debug_toolbar.panels.cache.CachePanel',
            'debug_toolbar.panels.signals.SignalsPanel',
            'debug_toolbar.panels.logging.LoggingPanel',
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ],
        children=[colander.SchemaNode(colander.String())]
    )
