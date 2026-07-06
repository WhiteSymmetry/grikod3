# -*- coding: utf-8 -*-
# setup.py

from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("grikod3.grikod3", ["grikod3/grikod3.py"]),
]

setup(
    ext_modules=cythonize(extensions, compiler_directives={'language_level': 3}),
)
