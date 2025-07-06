import os
import shutil

masaustu = os.path.join(os.path.expanduser("~"), "Desktop")
hedef_klasor = os.path.join(masaustu, "Oyunlar")

if not os.path.exists(hedef_klasor):
    os.makedirs(hedef_klasor)

oyun_anahtar_kelimeler = ["oyun", "game", "setup", "play", "launcher", "roblox", "steam"]
oyun_uzantilari = [".lnk", ".exe", ".url"]

for dosya in os.listdir(masaustu):
    tam_yol = os.path.join(masaustu, dosya)

    if tam_yol == hedef_klasor:
        continue

    dosya_adi_kucuk = dosya.lower()
    if any(k in dosya_adi_kucuk for k in oyun_anahtar_kelimeler) or \
       any(dosya_adi_kucuk.endswith(ext) for ext in oyun_uzantilari):
        try:
            shutil.move(tam_yol, hedef_klasor)
            print(f"Taşındı: {dosya}")
        except Exception as e:
            print(f"HATA ({dosya}): {e}")
