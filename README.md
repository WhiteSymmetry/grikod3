# grikod3 (Grikod, Gri Kod, Gray Code, GrayCode): binary ↔ grikod
---

# grikod3 <img src="https://github.com/WhiteSymmetry/grikod3/blob/main/docs/grikod3_logo.jpg" alt="logo" align="right" height="140"/>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15352206.svg)](https://doi.org/10.5281/zenodo.15352206)

[![WorkflowHub DOI](https://img.shields.io/badge/DOI-10.48546%2Fworkflowhub.datafile.13.1-blue)](https://doi.org/10.48546/workflowhub.datafile.13.1)

[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod3/badges/version.svg)](https://anaconda.org/bilgi/grikod3)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod3/badges/latest_release_date.svg)](https://anaconda.org/bilgi/grikod3)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod3/badges/platforms.svg)](https://anaconda.org/bilgi/grikod3)
[![Anaconda-Server Badge](https://anaconda.org/bilgi/grikod3/badges/license.svg)](https://anaconda.org/bilgi/grikod3)
[![Open Source](https://img.shields.io/badge/Open%20Source-Open%20Source-brightgreen.svg)](https://opensource.org/)
[![AGPL-3.0-or-later License](https://img.shields.io/badge/License-AGPL-3.0-or-later-yellow.svg)](https://opensource.org/licenses/AGPL-3.0-or-later)

[![Python CI](https://github.com/WhiteSymmetry/grikod3/actions/workflows/python_ci.yml/badge.svg?branch=main)](https://github.com/WhiteSymmetry/grikod3/actions/workflows/python_ci.yml)
[![codecov](https://codecov.io/gh/WhiteSymmetry/grikod3/graph/badge.svg?token=IT3XFZOSJD)](https://codecov.io/gh/WhiteSymmetry/grikod3)
[![Documentation Status](https://readthedocs.org/projects/grikod3/badge/?version=latest)](https://grikod3.readthedocs.io/en/latest/)
[![Binder](https://terrarium.evidencepub.io/badge_logo.svg)](https://terrarium.evidencepub.io/v2/gh/WhiteSymmetry/grikod3/HEAD)
[![PyPI version](https://badge.fury.io/py/grikod3.svg)](https://badge.fury.io/py/grikod3)
[![PyPI Downloads](https://static.pepy.tech/badge/grikod3)](https://pepy.tech/projects/grikod3)
[![Linted with Ruff](https://img.shields.io/badge/Linted%20with-Ruff-green?logo=python&logoColor=white)](https://github.com/astral-sh/ruff)

---

<p align="left">
    <table>
        <tr>
            <td style="text-align: center;">PyPI</td>
            <td style="text-align: center;">
                <a href="https://pypi.org/project/grikod3/">
                    <img src="https://badge.fury.io/py/grikod3.svg" alt="PyPI version" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">Conda</td>
            <td style="text-align: center;">
                <a href="https://anaconda.org/bilgi/grikod3">
                    <img src="https://anaconda.org/bilgi/grikod3/badges/version.svg" alt="conda-forge version" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">DOI</td>
            <td style="text-align: center;">
                <a href="https://doi.org/10.5281/zenodo.15352206">
                    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.15352206.svg" alt="DOI" height="18"/>
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;">License: AGPL-3.0-or-later</td>
            <td style="text-align: center;">
                <a href="https://opensource.org/licenses/AGPL-3.0-or-later">
                    <img src="https://img.shields.io/badge/License-AGPL-3.0-or-later-yellow.svg" alt="License" height="18"/>
                </a>
            </td>
        </tr>
    </table>
</p>

---
A Python library for converting binary numbers to Gray Code with ease.

---

## Tanım (Türkçe)
Gri Kod: grikod3 İkili sayıları Gri Koda çevirir.

## Description (English)
Gri Kod: grikod3 converts binary numbers to Gray Code.

---

## Kurulum (Türkçe) / Installation (English)

### Python ile Kurulum / Install with pip, conda, mamba
```bash
pip install grikod3 -U
python -m pip install -U grikod3
conda install bilgi::grikod3 -y
mamba install bilgi::grikod3 -y
```

```diff
- pip uninstall grikod3 -y
+ pip install -U grikod3
+ python -m pip install -U grikod3
```

[PyPI](https://pypi.org/project/grikod3/)

### Test Kurulumu / Test Installation

```bash
pip install -i https://test.pypi.org/simple/ grikod3 -U
```

### Github Master Kurulumu / GitHub Master Installation

**Terminal:**

```bash
pip install git+https://github.com/WhiteSymmetry/grikod3.git
```

**Jupyter Lab, Notebook, Visual Studio Code:**

```python
!pip install git+https://github.com/WhiteSymmetry/grikod3.git
# or
%pip install git+https://github.com/WhiteSymmetry/grikod3.git
```

---

## Kullanım (Türkçe) / Usage (English)

```python
import grikod3
grikod3.__version__
```

```python
import grikod3
grikod3.ikili_2_gri_kod("1010")
```

```python
import grikod3

def main():
    # Binary numbers: ikili sayılar
    binary_numbers = ["0", "1", "10", "11", "100", "101", "1111"]

    for binary in binary_numbers:
        try:
            gray_code = grikod3.ikili_2_gri_kod(binary)
            print(f"Binary: İkili: {binary} -> Gri Kod: {gray_code}")
        except grikod3.InvalidBinaryError as e:
            print(f"İkili: {binary} -> Hata: {e}")

if __name__ == "__main__":
    main()
```
```
Binary: İkili: 0 -> Gri Kod: 0
Binary: İkili: 1 -> Gri Kod: 1
Binary: İkili: 10 -> Gri Kod: 11
Binary: İkili: 11 -> Gri Kod: 10
Binary: İkili: 100 -> Gri Kod: 110
Binary: İkili: 101 -> Gri Kod: 111
Binary: İkili: 1111 -> Gri Kod: 1000


#Input: 100
#Output example
#000:000
#001:001
#010:011
#011:010
#100:110
#101:111
#110:101
#111:100
```

# Graycode-Binary & Binary-Graycode

```python
from grikod2 import ikili_2_gri_kod
grikod2.ikili_2_gri_kod("1010")
```

```python
from grikod3 import ikili_2_gri_kod, grikod2ikili, run_interactive_converter
# Örnek kullanımlar:
print(grikod2ikili("1011"))   # Çıktı: "1101" (doğrulama: 1011 gri kodu 1101 ikiliğe denk gelir)
print(grikod2ikili("0"))      # "0"
print(grikod2ikili("111"))    # "101"
```

```python
from grikod3 import ikili_2_gri_kod, grikod2ikili, run_interactive_converter
run_interactive_converter()
```

```python
import grikod3

def main():
    print("🌟 Gri Kod Dönüştürücü - grikod3 Paketi ile")
    print("Geçerli bir ikili sayı girin (örneğin: 1101)")
    print("Çıkmak için 'q' yazın.\n")

    while True:
        user_input = input("İkili sayı: ").strip()

        if user_input.lower() == 'q':
            print("👋 Çıkılıyor. İyi günler!")
            break

        try:
            gray_code = grikod3.ikili_2_gri_kod(user_input)
            print(f"✅ Gri Kod: {gray_code}\n")
        except grikod3.InvalidBinaryError as e:
            print(f"❌ Giriş Hatası: {e}\n")
        except Exception as e:
            print(f"⚠️ Beklenmeyen hata: {e}\n")

if __name__ == "__main__":
    main()
```

```python
import grikod3

if __name__ == "__main__":
    print("🚀 grikod3 Etkileşimli Moduna Hoş Geldiniz!")
    grikod3.run_interactive_converter()
```

---

### Development
```bash
# Clone the repository
git clone https://github.com/WhiteSymmetry/grikod3.git
cd grikod3

# Install in development mode
python -m pip install -ve . # Install package in development mode

# Run tests
pytest

Notebook, Jupyterlab, Colab, Visual Studio Code
!python -m pip install git+https://github.com/WhiteSymmetry/grikod3.git
```
---

## Citation

If this library was useful to you in your research, please cite us. Following the [GitHub citation standards](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files), here is the recommended citation.

### BibTeX


### APA

```
Keçeci, M. (2025). grikod3 [Data set]. WorkflowHub. https://doi.org/10.48546/workflowhub.datafile.13.1

Keçeci, M. (2025). grikod3. GitHub, PYPI, Anaconda, Zenodo. https://doi.org/10.5281/zenodo.15352206

```

### Chicago

```
Keçeci, Mehmet. grikod3 [Data set]. WorkflowHub. https://doi.org/10.48546/workflowhub.datafile.13.1

Keçeci, Mehmet. "grikod3". Zenodo, 06 Mayıs 2025. https://doi.org/10.5281/zenodo.15352206

```


### Lisans (Türkçe) / License (English)

```
This project is licensed under the AGPL-3.0-or-later License.

```

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FWhiteSymmetry%2Fgrikod3.svg?type=shield&issueType=license)](https://app.fossa.com/projects/git%2Bgithub.com%2FWhiteSymmetry%2Fgrikod3?ref=badge_shield&issueType=license)

# Pixi:

[![Pixi](https://img.shields.io/badge/Pixi-Pixi-brightgreen.svg)](https://prefix.dev/channels/bilgi)

pixi init grikod3

cd grikod3

pixi workspace channel add https://repo.prefix.dev/bilgi --prepend

✔ Added https://repo.prefix.dev/bilgi

pixi add grikod3

✔ Added grikod3 >=0.1.0,<2

pixi install

pixi shell

pixi run python -c "import grikod3; print(grikod3.__version__)"

### Çıktı: 0.1.0

pixi remove grikod3

conda install -c https://prefix.dev/bilgi grikod3

pixi run python -c "import grikod3; print(grikod3.__version__)"

### Çıktı: 0.1.0

pixi run pip list | grep grikod3

### grikod3  0.1.0

pixi run pip show grikod3

Name: grikod3

Version: 0.1.0

Summary: Converts binary numbers to Gray Code. grikod3 (Gray Code, Grey Code)

Home-page: https://github.com/WhiteSymmetry/grikod3

Author: Mehmet Keçeci

Author-email: Mehmet Keçeci <...>

License: AGPL-3.0-or-later License

Copyright (c) 2025 Mehmet Keçeci

