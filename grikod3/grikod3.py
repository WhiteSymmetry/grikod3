class InvalidBinaryError(ValueError):
    """Geçersiz ikili girişler için özel hata sınıfı."""
    pass

def ikili_2_gri_kod(i2grik: str) -> str:
    """İkili bir string'i ilgili Gri Koduna dönüştürür."""
    if not i2grik:
        raise InvalidBinaryError("Hata: Giriş boş olamaz.")
    if not all(c in '01' for c in i2grik):
        raise InvalidBinaryError("Hata: Lütfen geçerli bir ikili sayı girin (sadece '0' ve '1' içermeli).")
    if len(i2grik) > 64:
        raise InvalidBinaryError("Hata: İkili sayı çok uzun (maksimum 64 bit).")
    try:
        i2grikod = int(i2grik, 2)
    except ValueError:
        raise InvalidBinaryError("Hata: İkili sayıya dönüştürme sırasında beklenmedik bir hata.")
    i2grikod ^= (i2grikod >> 1)
    return bin(i2grikod)[2:].zfill(len(i2grik))

# --- İnteraktif Mod Fonksiyonu ---

def run_interactive_converter():
    """İnteraktif Gri Kod dönüştürücü konsolunu başlatır."""
    print("GriKod2 Dönüştürücü - İnteraktif Mod")
    print("Çıkmak için 'q' girin.")

    while True:
        i2grik_input = input("İkili bir sayı girin: ")
        if i2grik_input.lower() == 'q':
            print("Çıkılıyor...")
            break
        try:
            # Yukarıda tanımlanan ana fonksiyonu kullan
            gri_kod_result = ikili_2_gri_kod(i2grik_input)
            print("Gri Kod2:", gri_kod_result)
        except InvalidBinaryError as e:
            print(e)
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}")

# --- Doğrudan Çalıştırma Bloğu ---
# Bu dosya `python grikod2.py` ile çalıştırıldığında interaktif modu başlatır.
# `import grikod2` ile import edildiğinde BU BLOK ÇALIŞMAZ.
if __name__ == "__main__":
    run_interactive_converter()
