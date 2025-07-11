import os
import shutil

# Klasör yolları
masaustu = os.path.join(os.path.expanduser("~"), "Desktop")
hedef_klasor = os.path.join(masaustu, "Oyunlar")

# 1. Oyunlar klasörünü oluştur
if not os.path.exists(hedef_klasor):
    os.makedirs(hedef_klasor)

# 2. Klasöre simge ata
simge_kaynak = "C:/Icons/joystick.ico"  # Bu .ico dosyasını önceden oraya koy!
simge_hedef = os.path.join(hedef_klasor, "joystick.ico")

if not os.path.exists(simge_hedef):
    shutil.copy(simge_kaynak, simge_hedef)

desktop_ini_yolu = os.path.join(hedef_klasor, "desktop.ini")
with open(desktop_ini_yolu, "w") as f:
    f.write(f"[.ShellClassInfo]\nIconResource=joystick.ico,0")

os.system(f'attrib +s +h "{hedef_klasor}"')
os.system(f'attrib +h "{desktop_ini_yolu}"')

# 3. Oyunları taşı
oyun_kelimeleri = ["oyun", "game", "launcher", "roblox", "steam", "gta", "valorant", "minecraft"]
oyun_uzantilari = [".lnk", ".exe", ".url", ".bat"]

for isim in os.listdir(masaustu):
    tam_yol = os.path.join(masaustu, isim)
    
    if tam_yol == hedef_klasor:
        continue  # Kendi klasörünü elleme
    
    isim_kucuk = isim.lower()
    bir_oyun_mu = False

    if os.path.isdir(tam_yol):
        if any(k in isim_kucuk for k in oyun_kelimeleri):
            bir_oyun_mu = True

    elif os.path.isfile(tam_yol):
        if any(isim_kucuk.endswith(ext) for ext in oyun_uzantilari) or \
           any(k in isim_kucuk for k in oyun_kelimeleri):
            bir_oyun_mu = True

    if bir_oyun_mu:
        try:
            shutil.move(tam_yol, os.path.join(hedef_klasor, isim))
            print(f"🎮 Taşındı: {isim}")
        except Exception as e:
            print(f"⚠️ HATA ({isim}): {e}")

input("\n✅ İşlem tamamlandı. Kapatmak için Enter'a bas...")

