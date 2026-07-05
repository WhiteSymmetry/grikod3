from setuptools import setup, find_packages

setup(
    name="grikod3",
    use_scm_version=True,  # Sürüm bilgisini setuptools_scm ile alır
    setup_requires=["setuptools", "wheel", "setuptools_scm"],  # Gerekli kurulum bağımlılıkları
    version='0.1.0',
    packages=find_packages(where="grikod3"),  # grikod3 dizinindeki modülleri bul
    package_dir={"": "grikod3"},  # grikod3 dizinine yönlendirme
    include_package_data=True,  # Ek dosyaları dahil et
    install_requires=[
        # Projenizin bağımlılıklarını buraya ekleyin
    ],
    author="Mehmet Keçeci",
    description="Binary to Gray code conversion package for efficient data encoding.",
    url="https://github.com/WhiteSymmetry/grikod3",
    license="AGPL-3.0-or-later",
    python_requires='>=3.10',
)
