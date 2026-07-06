# -*- coding: utf-8 -*-
# setup.py

import sys
import platform
from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("grikod3.grikod3", ["grikod3/grikod3.py"]),
]

setup(
    ext_modules=cythonize(extensions, compiler_directives={'language_level': 3}),
)


ext = Extension(
    name=f"grikod3.grikod3_{platform.system()}_py{sys.version_info.major}{sys.version_info.minor}",
    sources=["grikod3/grikod3.py"]
)
