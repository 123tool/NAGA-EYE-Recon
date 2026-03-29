# 🐉 NAGA-EYE: High-Speed OSINT Recon
**Next-Generation Account Finder by SPY-E & 123Tool**

NAGA-EYE adalah mesin OSINT (Open Source Intelligence) yang dirancang untuk mencari profil digital seseorang berdasarkan **Username** atau **Email** secara instan. Menggunakan arsitektur *Asynchronous I/O*, alat ini mampu melakukan pemindaian ratusan platform sekaligus tanpa lag.

## ✨ Fitur Utama
- **⚡ Ultra Fast**: Menggunakan `aiohttp` untuk pemindaian paralel.
- **🎯 Dual Target**: Support pencarian berdasarkan Username maupun Email.
- **🛡️ Stealth Mode**: Rotasi otomatis User-Agent untuk menghindari blokir firewall.
- **📱 Multi Platform**: Support Termux, Windows (CMD/PowerShell), Linux, dan macOS.

## ⚙️ Instalasi

### 1. Persiapan (Semua Perangkat)
Pastikan Python 3.8+ sudah terinstall.

### 2. Instalasi Library
Buka terminal dan jalankan:
```bash
pip install aiohttp fake-useragent
git clone [https://github.com/123tool/NAGA-EYE-Recon.git](https://github.com/123tool/NAGA-EYE-Recon.git)
cd NAGA-EYE-Recon
python naga_eye.py
```
### 3. Cara Penggunaan
​Jalankan script: python naga_eye.py
​Masukkan target (Contoh: johndoe atau johndoe@email.com)
​Tunggu hingga proses Scanning selesai.
​Hasil akan muncul dengan status [FOUND] jika akun terdeteksi.

## ​⚠️ Disclaimer
***​Project ini dibuat oleh SPY-E & 123Tool hanya untuk tujuan edukasi dan audit keamanan. Segala bentuk penyalahgunaan adalah tanggung jawab pengguna masing-masing.
​Trademark by SPY-E & 123Tool Premium Tools***
