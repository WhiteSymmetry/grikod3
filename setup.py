from setuptools import setup
from Cython.Build import cythonize

# Buraya derlemek istediğiniz .py dosyasının adını yazın
# Örnek: "benim_modulum.py" veya birden fazla dosya için ["mod1.py", "mod2.py"]
setup(
    ext_modules=cythonize("grikod3/grikod3.py"),
    zip_safe=False,
)
