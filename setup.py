#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='cassis-autolink',
      version='0.1',
      description='Python port of (a subset of) CASSIS',
      author='Kyle Mahan',
      author_email='kyle@kylewm.com',
      url='https://github.com/kylewm/cassis-autolink-py/',
      py_modules=['cassis'],
      test_suite='cassistest'
)
