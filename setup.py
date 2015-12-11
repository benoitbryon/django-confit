#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python packaging."""
import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    """Test command that runs tox."""
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox  # import here, cause outside the eggs aren't loaded.
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


#: Absolute path to directory containing setup.py file.
here = os.path.abspath(os.path.dirname(__file__))
#: Boolean, ``True`` if environment is running Python version 2.
IS_PYTHON2 = sys.version_info[0] == 2


NAME = 'django-confit'
README = open(os.path.join(here, 'README.rst')).read()
DESCRIPTION = 'Django settings loaders and validators, with local flavour.'
VERSION = open(os.path.join(here, 'VERSION')).read().strip()
AUTHOR = u'Benoît Bryon'
EMAIL = 'benoit@marmelune.net'
URL = 'https://django-confit.readthedocs.org'
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.3",
    "Framework :: Django",
]
KEYWORDS = [
    'configuration',
    'settings',
    'schema',
    'validation',
    'yaml',
    'json',
]
PACKAGES = [NAME.replace('-', '_')]
REQUIREMENTS = [
    'colander',
    'Django>=1.5',
    'PyYAML',
    'setuptools',
    'six',
]
if IS_PYTHON2:
    REQUIREMENTS.extend(['mock'])
ENTRY_POINTS = {}
LICENSE = 'BSD'
TEST_REQUIREMENTS = ['tox']
CMDCLASS = {'test': Tox}


if __name__ == '__main__':  # Do not run setup() when we import this module.
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=README,
        classifiers=CLASSIFIERS,
        keywords=' '.join(KEYWORDS),
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
        install_requires=REQUIREMENTS,
        entry_points=ENTRY_POINTS,
        tests_require=TEST_REQUIREMENTS,
        cmdclass=CMDCLASS,
    )
