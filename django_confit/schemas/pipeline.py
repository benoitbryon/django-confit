"""Configuration schema for django-pipeline."""
import colander


class ConfigurationSchema(colander.MappingSchema):
    """Configuration schema for django-pipeline.

    Reference is
    https://github.com/cyberdelia/django-pipeline/blob/master/pipeline/conf.py

    """
    PIPELINE_CLOSURE_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='',
    )
    PIPELINE_CLOSURE_BINARY = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='/usr/bin/env closure',
    )
    PIPELINE_COFFEE_SCRIPT_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='',
    )
    PIPELINE_COFFEE_SCRIPT_BINARY = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='/usr/bin/env coffee',
    )
    PIPELINE_COMPILERS = colander.SchemaNode(
        colander.Sequence(),
        missing=colander.drop,
        default=[],
        children=[colander.SchemaNode(colander.String())]
    )
    PIPELINE_CSS = colander.SchemaNode(
        colander.Mapping(unknown='preserve'),
        missing=colander.null,
        default={},
        children=[
            colander.SchemaNode(
                colander.Mapping(unknown='ignore'),
                missing=colander.drop,
                default={},
                children=[
                    colander.SchemaNode(
                        colander.Sequence(),
                        name='source_filenames',
                        missing=colander.required,
                        default=[],
                        children=[colander.SchemaNode(colander.String())]
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='output_filename',
                        missing=colander.required,
                        default='',
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='variant',
                        missing=colander.drop,
                        default=colander.null,
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='template_name',
                        missing=colander.drop,
                        default=colander.null,
                    ),
                    colander.SchemaNode(
                        colander.Mapping(unknown='preserve'),
                        name='extra_context',
                        missing=colander.drop,
                        default={},
                    ),
                    colander.SchemaNode(
                        colander.Boolean(),
                        name='manifest',
                        missing=colander.drop,
                        default=True,
                    ),
                ]
            ),
        ]
    )
    PIPELINE_CSS_COMPRESSOR = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='pipeline.compressors.yuglify.YuglifyCompressor',
    )
    PIPELINE_CSSMIN_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='',
    )
    PIPELINE_CSSMIN_BINARY = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='/usr/bin/env cssmin',
    )
    PIPELINE_CSSTIDY_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='--template=highest',
    )
    PIPELINE_CSSTIDY_BINARY = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='/usr/bin/env csstidy',
    )
    PIPELINE_DISABLE_WRAPPER = colander.SchemaNode(
        colander.Boolean(),
        missing=colander.drop,
        default=False,
    )
    PIPELINE_EMBED_MAX_IMAGE_SIZE = colander.SchemaNode(
        colander.Integer(),
        missing=colander.drop,
        default=32700,
    )
    PIPELINE_EMBED_PATH = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='[/]?embed/',
    )
    PIPELINE_ENABLED = colander.SchemaNode(
        colander.Boolean(),
        missing=colander.drop,
        default=colander.null,
    )
    PIPELINE_JS = colander.SchemaNode(
        colander.Mapping(unknown='preserve'),
        missing=colander.null,
        default={},
        children=[
            colander.SchemaNode(
                colander.Mapping(unknown='ignore'),
                missing=colander.drop,
                default={},
                children=[
                    colander.SchemaNode(
                        colander.Sequence(),
                        name='source_filenames',
                        missing=colander.required,
                        default=[],
                        children=[colander.SchemaNode(colander.String())]
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='output_filename',
                        missing=colander.required,
                        default='',
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='variant',
                        missing=colander.drop,
                        default=colander.null,
                    ),
                    colander.SchemaNode(
                        colander.String(),
                        name='template_name',
                        missing=colander.drop,
                        default=colander.null,
                    ),
                    colander.SchemaNode(
                        colander.Mapping(unknown='preserve'),
                        name='extra_context',
                        missing=colander.drop,
                        default={},
                    ),
                    colander.SchemaNode(
                        colander.Boolean(),
                        name='manifest',
                        missing=colander.drop,
                        default=True,
                    ),
                ]
            ),
        ]
    )
    PIPELINE_JS_COMPRESSOR = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='pipeline.compressors.yuglify.YuglifyCompressor',
    )
    PIPELINE_LESS_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='',
    )
    PIPELINE_LESS_BINARY = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='/usr/bin/env lessc',
    )
    PIPELINE_LIVE_SCRIPT_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='',
    )
    PIPELINE_LIVE_SCRIPT_BINARY = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='/usr/bin/env lsc',
    )
    PIPELINE_MIMETYPES = colander.SchemaNode(
        colander.Sequence(),
        missing=colander.drop,
        default=(
            ('text/coffeescript', '.coffee'),
            ('text/less', '.less'),
            ('text/javascript', '.js'),
            ('text/x-sass', '.sass'),
            ('text/x-scss', '.scss'),
        ),
        children=[
            colander.SchemaNode(
                colander.Tuple(),
                missing=colander.drop,
                default=colander.null,
                children=[
                    colander.SchemaNode(colander.String()),
                    colander.SchemaNode(colander.String()),
                ]
            ),
        ]
    )
    PIPELINE_ROOT = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default=colander.null,
    )
    PIPELINE_SASS_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='--update',
    )
    PIPELINE_SASS_BINARY = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='/usr/bin/env sass',
    )
    PIPELINE_STORAGE = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='pipeline.storage.PipelineFinderStorage',
    )
    PIPELINE_STYLUS_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='',
    )
    PIPELINE_STYLUS_BINARY = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='/usr/bin/env stylus',
    )
    PIPELINE_TEMPLATE_EXT = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='.jst',
    )
    PIPELINE_TEMPLATE_FUNC = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='template',
    )
    PIPELINE_TEMPLATE_NAMESPACE = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='window.JST',
    )
    PIPELINE_TEMPLATE_SEPARATOR = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='_',
    )
    PIPELINE_UGLIFYJS_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='',
    )
    PIPELINE_UGLIFYJS_BINARY = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='/usr/bin/env uglifyjs',
    )
    PIPELINE_URL = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default=colander.null,
    )
    PIPELINE_YUGLIFY_BINARY = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='/usr/bin/env yuglify',
    )
    PIPELINE_YUGLIFY_CSS_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='--terminal',
    )
    PIPELINE_YUGLIFY_JS_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='--terminal',
    )
    PIPELINE_YUI_BINARY = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='/usr/bin/env yuicompressor',
    )
    PIPELINE_YUI_CSS_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='',
    )
    PIPELINE_YUI_JS_ARGUMENTS = colander.SchemaNode(
        colander.String(),
        missing=colander.drop,
        default='',
    )
