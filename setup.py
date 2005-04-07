#!/usr/bin/env python

"""autolog: quick logging setup

Autolog makes the standard Python logging module easier to set up.
"""

__version__ = "0.1.0"

from distutils.core import setup

doclines = __doc__.splitlines()
name, short_description = doclines[0].split(": ")
long_description = "\n".join(doclines[2:])

setup(name=name,
      version=__version__,
      description=short_description,
      author="Michael Hoffman",
      author_email="hoffman@ebi.ac.uk",
      url="http://www.ebi.ac.uk/~hoffman/software/",
      license="GNU GPL",
      long_description = long_description,
      package_dir = {'': 'lib'},
      py_modules = ['autolog']
      )
