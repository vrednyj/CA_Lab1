#!/usr/bin/env python

from distutils.core import setup
import shutil

with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open('__version__.py').read())

setup(name='CA_Lab1',
      version=__version__,
      description='Lab for DevOps Software',
      author='Vitalijus Baseckas',
      author_email='L00169827@student.lyit.ie',
      url='https://github.com/vrednyj/CA_Lab1',
      packages=['CA_Lab1'],
      scripts=['tests.py'],
      long_description="A collection of classes that can be used to decom network or PCM based FTI traffic",
      classifiers =['Programming Language :: Python',
                    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                    'Operating System :: OS Independent',
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'Topic :: Software Development :: Libraries :: Python Modules',
                    ],
     )
