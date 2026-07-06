# __init__.py

from __future__ import annotations

import importlib
import warnings
import os
import types

__version__ = "0.1.5"

# ---- 1. Modül yüklemeyi dene (önce derlenmiş, sonra kaynak) ----
try:
    # Derlenmiş uzantıyı (grikod3.so/.pyd) dene
    from . import grikod3 as _impl
except ImportError:
    # Derlenmiş dosya yoksa, fallback kaynak dosyayı dene
    try:
        from . import grikod3_fallback as _impl
    except ImportError as e:
        # Hiçbiri yoksa uyarı ver ve boş bir yedek oluştur
        warnings.warn(
            f"Ne derlenmiş uzantı ne de fallback dosyası bulunamadı: {e}",
            ImportWarning
        )
        # Boş bir modül oluştur (çökmeyi önlemek için)
        _impl = types.ModuleType("grikod3")
        _impl.ikili_2_gri_kod = lambda x: None
        _impl.grikod2ikili = lambda x: None
        _impl.run_interactive_converter = lambda: None
        _impl.InvalidBinaryError = ValueError

# ---- 2. Ana fonksiyonları içe aktar ----
try:
    ikili_2_gri_kod = _impl.ikili_2_gri_kod
    grikod2ikili = _impl.grikod2ikili
    run_interactive_converter = _impl.run_interactive_converter
    InvalidBinaryError = _impl.InvalidBinaryError
except AttributeError as e:
    warnings.warn(f"Modül gerekli nitelikleri içermiyor: {e}", ImportWarning)
    # Varsayılan değerler (hata durumunda)
    ikili_2_gri_kod = None
    grikod2ikili = None
    run_interactive_converter = None
    InvalidBinaryError = ValueError

# ---- 3. Eski fonksiyon (deprecated) ----
def eski_fonksiyon():
    warnings.warn(
        "eski_fonksiyon() artık kullanılmamaktadır...",
        category=DeprecationWarning,
        stacklevel=2
    )

# ---- 4. Geliştirme modu (yeniden yükleme) ----
if os.getenv("DEVELOPMENT") == "true":
    try:
        importlib.reload(_impl)
    except Exception as e:
        warnings.warn(f"Geliştirme modunda yeniden yükleme başarısız: {e}", ImportWarning)

# ---- 5. __all__ listesi ----
__all__ = [
    "ikili_2_gri_kod",
    "grikod2ikili",
    "run_interactive_converter",
    "InvalidBinaryError",
    "__version__",
]
