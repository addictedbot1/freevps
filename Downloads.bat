@echo off

# Unduh file utama
curl -L -o login.py https://www.dropbox.com/scl/fi/az5jzhpuiylnw7yqw9du5/login.py?rlkey=1qjxif8fu35dh0v77nagv2ihh&dl=0
curl -L -o rustdesk.exe https://github.com/rustdesk/rustdesk/releases/download/1.2.1/rustdesk-1.2.1-x86_64.exe

# Install dependencies
pip install pyautogui psutil --quiet

# Install Telegram
curl -L -o C:\Public\Telegram.exe https://telegram.org/dl/desktop/win64
start /wait C:\Public\Telegram.exe /VERYSILENT
del C:\Public\Telegram.exe

# Hapus shortcut tidak perlu
del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk" 2> nul
del /f "C:\Users\Public\Desktop\Unity Hub.lnk" 2> nul

# Set password untuk akun Windows
set password=@#Disala123456
powershell -Command "Set-LocalUser -Name 'runneradmin' -Password (ConvertTo-SecureString -AsPlainText '%password%' -Force)"

# Konfigurasi sistem
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel" /v "{20D04FE0-3AEA-1069-A2D8-08002B30309D}" /t REG_DWORD /d 0 /f
tzutil /s "Sri Lanka Standard Time"

# Jalankan RustDesk & automation
start "" /high rustdesk.exe
timeout /t 10
python login.py
