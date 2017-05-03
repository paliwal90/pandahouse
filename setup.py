#!/usr/bin/env python

from os.path import exists
from setuptools import setup

setup(name='pandahouse',
      version='0.1',
      description='Pandas interface for Clickhouse HTTP API',
      url='http://github.com/kszucs/pandahouse',
      maintainer='Krisztian Szucs',
      maintainer_email='szucs.krisztian@gmail.com',
      license='BSD',
      keywords='',
      packages=['pandahouse'],
      tests_require=['pytest'],
      setup_requires=['pytest-runner'],
      install_requires=['pandas', 'requests'],
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      zip_safe=False)