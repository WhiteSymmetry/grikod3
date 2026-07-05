# __init__.py

from __future__ import annotations

import importlib
import warnings
import os

# Geliştirme modunda yeniden yükleme (isteğe bağlı)
if os.getenv("DEVELOPMENT") == "true":
    try:
        import grikod3.grikod3
        importlib.reload(grikod3.grikod3)
    except (ImportError, KeyError):
        pass

# Doğru modül adıyla içe aktarım yapın: grikod3.py → .grikod3
try:
    from .grikod3 import ikili_2_gri_kod, run_interactive_converter, InvalidBinaryError
except ImportError as e:
    warnings.warn(f"Gerekli modül yüklenemedi: {e}", ImportWarning)

__all__ = ["ikili_2_gri_kod", "run_interactive_converter", "InvalidBinaryError"]

__version__ = "1.1.4"

def eski_fonksiyon():
    warnings.warn(
        "eski_fonksiyon() artık kullanılmamaktadır...",
        category=DeprecationWarning,
        stacklevel=2
    )
