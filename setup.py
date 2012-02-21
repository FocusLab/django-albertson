#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError, err:
    from distutils.core import setup

from dj_albertson import VERSION

setup(
    name='django-albertson',
    version=".".join(map(str, VERSION)),
    description="Integration library for Django and Albertson.",
    author="Sean O'Connor",
    author_email="sean@focuslab.io",
    url="https://github.com/FocusLab/django-albertson",
    packages=['dj_albertson'],
    license="BSD",
    long_description=open('README.rst').read(),
    install_requires=['albertson', 'django'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
