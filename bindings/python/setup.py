#!/usr/bin/env python
 
from distutils.core import setup
from distutils.extension import Extension
 
setup(name="PackageName",
    ext_modules=[
        Extension("psf", ["psfpython.cc"],
        libraries = ["boost_python", "psf"],
        library_dirs = ['.'])
    ])
