# -*- coding: utf-8 -*-
"""Utilities to load configuration from various sources:

* from :attr:`os.environ` or similar dictionary:
  :func:`settings_from_string_mapping`;

* from Python module: :func:`settings_from_module`;

* from JSON or YAML file: :func:`settings_from_file`.

"""
import json

import six
import yaml


def load_mapping(input, prefix=''):
    """Convert mapping of {key: string} to {key: complex type}.

    This function makes it possible (and easy) to load complex types from
    single-level key-value stores, such as environment variables or INI files.

    Of course, both flat and nested mappings are supported:

    >>> from django_confit import load_mapping
    >>> flat_mapping = {'DEBUG': 'True', 'SECRET_KEY': 'not a secret'}
    >>> output = load_mapping(flat_mapping)
    >>> output == flat_mapping
    True

    >>> nested_mapping = {'DATABASES': {'USER': 'me', 'HOST': 'localhost'}}
    >>> output = load_mapping(nested_mapping)
    >>> output == nested_mapping
    True

    Values can be complex types (sequences, mappings) using JSON or YAML.
    Keys using ".json" or ".yaml" suffix are automatically decoded:

    >>> nested_mapping = {
    ...     'DATABASES.yaml': 'ENGINE: sqlite3',
    ... }
    >>> output = load_mapping(nested_mapping)
    >>> output['DATABASES'] == {'ENGINE': 'sqlite3'}
    True

    You can use optional ``prefix`` argument to load only a subset of mapping:

    >>> mapping = {'YES_ONE': '1', 'NO_TWO': '2'}
    >>> load_mapping(mapping, prefix='YES_')
    {'ONE': '1'}

    """
    output = {}
    for key, value in six.iteritems(input):
        if key.startswith(prefix):
            key = key[len(prefix):]
            if key.endswith('.json'):
                output[key[:-5]] = json.loads(value)
            elif key.endswith('.yaml'):
                output[key[:-5]] = yaml.load(value)
            else:
                output[key] = value
    return output


def load_file(file_obj):
    """Return mapping from file object, using ``name`` attr to guess format.

    Supported file formats are JSON and YAML. The lowercase extension is used
    to guess the file type.

    >>> from django_confit import load_file
    >>> from six.moves import StringIO
    >>> file_obj = StringIO('SOME_LIST: [a, b, c]')
    >>> file_obj.name = 'something.yaml'
    >>> load_file(file_obj) == {
    ...     'SOME_LIST': ['a', 'b', 'c'],
    ... }
    True

    """
    file_name = file_obj.name
    if file_name.endswith('.yaml'):
        return yaml.load(file_obj)
    elif file_name.endswith('.json'):
        return json.load(file_obj)
    else:
        raise ValueError(
            'Cannot guess format of configuration file "{name}". '
            'Expected one of these extensions: "{extensions}".'.format(
                name=file_name,
                extensions='", "'.join('.yaml', '.json')))


def load_module(module_path):
    """Return module's globals as a dict.

    >>> from django_confit import load_module
    >>> settings = load_module('django.conf.global_settings')
    >>> settings['DATABASES']
    {}

    It does not load "protected" and "private" attributes (those with
    underscores).

    >>> '__name__' in settings
    False

    """
    module = __import__(module_path, fromlist='*', level=0)
    is_uppercase = lambda x: x.upper() == x
    is_special = lambda x: x.startswith('_')
    return dict([(key, value) for key, value in module.__dict__.items()
                 if is_uppercase(key) and not is_special(key)])
