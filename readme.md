Clipping Studio Pro
Clipping Studio Pro adalah dashboard lokal berbasis Python Flask yang dirancang khusus untuk mempercepat alur kerja produksi konten Cuplikan Seru ID. Aplikasi ini memungkinkan pengunduhan cuplikan video YouTube secara presisi dan konversi video landscape ke portrait (9:16) untuk kebutuhan Reels atau TikTok.

🚀 Fitur Utama
YouTube Downloader & Trimmer: Mengunduh video berdasarkan rentang waktu (start & end) yang spesifik untuk menghindari pemborosan kuota dan ruang penyimpanan.

Dual-Mode Output: Mendukung pengunduhan langsung dalam format original (Landscape) atau otomatis di-crop menjadi format Portrait.

Manual Video Converter: Fitur untuk mengunggah video lokal dari folder mana pun di Mac dan mengubahnya menjadi format portrait.

Anti-Double Click Protection: Sistem pengunci tombol untuk mencegah beban CPU berlebih pada MacBook Air saat proses render video berlangsung.

🛠️ Prasyarat Sistem
Aplikasi ini berjalan secara lokal dan membutuhkan beberapa komponen berikut terinstal di MacBook Air kamu:

Python 3.13+

Flask: Sebagai framework web server.

yt-dlp: Mesin pengunduh video (terletak di /usr/local/bin/yt-dlp).

FFmpeg: Mesin pemroses dan konversi video (terletak di /usr/local/bin/ffmpeg).

📂 Struktur Proyek
yt-downloader-app/
├── app.py              # Logika backend Flask dan integrasi sistem
├── templates/
│   └── index.html      # Antarmuka dashboard (HTML/JavaScript/Tailwind)
├── .gitignore          # Daftar file yang diabaikan oleh Git
└── Clipper_Uploads/    # Folder otomatis untuk hasil konversi manual


⚙️ Cara Instalasi & Penggunaan
1. Persiapan Folder: Pastikan semua file berada dalam folder yt-downloader-app.

2. Instalasi Dependensi:
python3 -m pip install flask

3. Menjalankan Aplikasi:
- Buka Terminal atau Cursor.
- Jalankan perintah: python3 app.py.

4. Akses Dashboard: Buka browser dan akses http://127.0.0.1:5000.

⚠️ Disclaimer
Aplikasi ini ditujukan untuk penggunaan pribadi dan efisiensi produksi konten. Pastikan untuk selalu mematuhi hak cipta dan kebijakan penggunaan layanan YouTube saat mengunduh konten.