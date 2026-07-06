# -*- coding: utf-8 -*-
# setup.py

# -*- coding: utf-8 -*-
from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name="grikod3.grikod3",          # Sabit kalmalı, import edilecek ad
        sources=["grikod3/grikod3.py"],  # Kaynak dosyanın yolu
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={'language_level': 3},  # Python 3 sözdizimi
    ),
    zip_safe=False,
)
