#!/usr/bin/env python

from distutils.core import setup
from version import __version__

setup(name='CCS Crawler Base',
      version=__version__,
      description='Utilities to be used with any crawler',
      author='Caio Caçador da Silva',
      author_email='caiocacador.s@gmail.com',
      url='https://github.com/caio-cacador/ccs-crawler-base',
      packages=['crawler_base'])
