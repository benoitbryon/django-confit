# -*- coding: utf-8 -*-
"""Helpers to manage local (project-level, environment-level) settings."""
import pkg_resources


#: Module version, as defined in PEP-0396.
__version__ = pkg_resources.get_distribution(__package__.replace('-', '_')) \
                           .version


# API shortcuts.
from django_confit.api import *  # NoQA
