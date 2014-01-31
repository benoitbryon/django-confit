# -*- coding: utf-8 -*-
"""Python packaging."""
import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


here = os.path.abspath(os.path.dirname(__file__))


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


NAME = 'django-confit'
README = open(os.path.join(here, 'README.rst')).read()
DESCRIPTION = 'Django settings loaders and validators, with local flavour.'
VERSION = open(os.path.join(here, 'VERSION')).read().strip()
AUTHOR = u'Benoît Bryon'
AUTHOR_EMAIL = 'benoit@marmelune.net'
URL = 'https://github.com/benoitbryon/%s' % NAME
PACKAGES = [NAME.replace('-', '_')]
REQUIREMENTS = [
    'colander',
    'Django>=1.5,<1.6',
    'PyYAML',
    'setuptools',
    'six',
]
try:
    from unittest import mock  # NoQA
except ImportError:
    REQUIREMENTS.append('mock')
ENTRY_POINTS = {}
CLASSIFIERS = [
    "License :: OSI Approved :: BSD License",
    "Development Status :: 1 - Planning",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.3",
    "Framework :: Django",
],
KEYWORDS = ['configuration', 'settings', 'schema', 'validation', 'yaml',
            'json']
LICENSE = 'BSD'
TEST_REQUIREMENTS = ['tox']
CMDCLASS = {'test': Tox}


if __name__ == '__main__':  # Don't run setup() when we import this module.
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=README,
        classifiers=CLASSIFIERS,
        keywords=' '.join(KEYWORDS),
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
        install_requires=REQUIREMENTS,
        entry_points=ENTRY_POINTS,
        tests_require=TEST_REQUIREMENTS,
        cmdclass=CMDCLASS,
    )
