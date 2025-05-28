# Sherlock-Lite
```bash
┌───────────────────────────────────────────────────────────────┐
│                      SHERLOCK PLUS 🔎                         │
├───────────────────────────────────────────────────────────────┤
│  Sherlock Plus, bir kullanıcı adının 30'dan fazla sosyal     │
│  medya ve platformda kullanılıp kullanılmadığını tespit eden │
│  hafif, hızlı ve genişletilebilir bir Python aracıdır.       │
│                                                               │
│  Kullanıcı adı araştırmalarında OSINT (Açık Kaynak           │
│  İstihbarat) için mükemmel bir yardımcıdır.                   │
└───────────────────────────────────────────────────────────────┘

📦 Özellikler:
 - 30+ platformda kullanıcı adı kontrolü
 - Kolay JSON ile yeni platform ekleme
 - Hızlı ve kullanıcı dostu terminal çıktısı
 - Açık kaynak ve özelleştirilebilir

🖥️ Desteklenen İşletim Sistemleri:
 - Kali Linux ✅
 - Ubuntu / Debian ✅
 - Arch / Manjaro ✅
 - Windows 10/11 ✅
 - macOS ✅
 - Android (Termux) ✅

🔧 Gereksinimler:
 - Python 3.x
 - pip (Python paket yöneticisi)
 - `git` (kodu klonlamak için)

💡 Hemen başlamak için aşağı kaydır!
``
(Windows 10 / 11)----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:: Python indir ve kur: https://www.python.org/downloads/
:: "Add Python to PATH" seçeneğini kurulumda işaretle!

:: CMD veya PowerShell'de aşağıdakileri yaz:

git clone https://github.com/kullaniciadi/sherlock-plus.git
cd sherlock-plus
pip install -r requirements.txt
python sherlock.py


(Kali Linux / Ubuntu / Debian)---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Gerekli paketleri kur
sudo apt update
sudo apt install python3 python3-pip git -y

# Sherlock Plus'ı klonla ve çalıştır
git clone https://github.com/kullaniciadi/sherlock-plus.git
cd sherlock-plus
pip3 install -r requirements.txt
python3 sherlock.py


(macOS)--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Homebrew yüklü değilse:
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Python ve git yükle
brew install python git

# Sherlock Plus'ı indir
git clone https://github.com/kullaniciadi/sherlock-plus.git
cd sherlock-plus
pip3 install -r requirements.txt
python3 sherlock.py


(Android (Termux)----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Termux'u aç ve aşağıdakileri sırayla çalıştır

pkg update && pkg upgrade -y
pkg install git python -y

# Sherlock Plus'ı indir
git clone https://github.com/kullaniciadi/sherlock-plus.git
cd sherlock-plus
pip install -r requirements.txt
python sherlock.py


(Arch Linux / Manjaro / Garuda)--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Python, pip ve git kur
sudo pacman -S python python-pip git

# Sherlock Plus'ı indir ve çalıştır
git clone https://github.com/kullaniciadi/sherlock-plus.git
cd sherlock-plus
pip install -r requirements.txt
python sherlock.py
