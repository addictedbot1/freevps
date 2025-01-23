import pyautogui as pag
import time
import pyperclip

PASSWORD = "@#Disala123456"  # Password sesuai Downloads.bat

actions = [
    (109, 451, 2),  # Klik "Install"
    (589, 495, 2),  # Klik "Install" lagi
    (722, 429, 1),  # Klik "OK"
    (708, 22, 7),   # Buka menu
    (83, 170, 2),   # Pilih "Security"
    (465, 68, 2),   # Aktifkan autentikasi
    (798, 386, 2),  # Scroll ke bawah
    (415, 224, 2),  # Klik "Set Password"
    (291, 250, 2),  # Field password pertama
    (310, 338, 2),  # Field konfirmasi password
    (631, 427, 2),  # Klik "OK"
    (95, 22, 2),    # Buka tab ID
    (165, 168, 2),  # Klik kanan pada ID
    (199, 178, 2),  # Pilih "Select All"
    (138, 167, 2),  # Klik kanan lagi
    (163, 182, 2)   # Pilih "Copy"
]

time.sleep(5)  # Tunggu RustDesk terbuka

for x, y, duration in actions:
    if (x, y) in [(165, 168), (138, 167)]:
        pag.rightClick(x, y, duration=duration)
    else:
        pag.click(x, y, duration=duration)
    
    # Handle input password
    if (x, y) in [(291, 250), (310, 338)]:
        pyperclip.copy(PASSWORD)  # Salin password ke clipboard
        pag.hotkey('ctrl', 'v')   # Tempel dengan Ctrl+V
        time.sleep(1)

# Simpan ID & password ke file
rustdesk_id = pyperclip.paste()
with open("C:\\Users\\Public\\Desktop\\rustdesk_info.txt", "w") as f:
    f.write(f"ID: {rustdesk_id}\nPassword: {PASSWORD}")

print("Konfigurasi RustDesk selesai! Informasi tersimpan di desktop.")
