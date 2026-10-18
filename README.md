# SECURESTORE - Toko Alat Tulis Sederhana untuk Praktikum SAST

**1. Deskripsi Aplikasi**

SecureStore adalah aplikasi toko alat tulis sederhana berbasis Python yang menggunakan database SQLite. Aplikasi ini menyediakan fitur melihat dan mencari produk, membuat pesanan, melihat riwayat pesanan, serta simulasi pembayaran. Proyek ini dibuat untuk memenuhi praktikum DevSecOps, khususnya penerapan Static Application Security Testing (SAST) menggunakan Bandit dan otomatisasi pengujian melalui GitHub Actions.

**2. Teknologi yang Digunakan**

- **Python** : bahasa pemrograman untuk logika aplikasi.
- **SQLite** : database untuk menyimpan data produk, pesanan, dan pembayaran simulasi.
- **pytest** : menjalankan unit test aplikasi.
- **Bandit** : alat SAST untuk menganalisis pola kode Python yang berpotensi menimbulkan masalah keamanan.
- **GitHub Actions** : mengotomatisasi proses pengujian dan pemindaian keamanan kode.

Aplikasi ini menggunakan Python tanpa framework aplikasi khusus.

**3. Struktur Proyek**

| File | Fungsi |
|---|---|
| `app.py` | Menjalankan menu utama aplikasi toko. |
| `store.py` | Mengelola produk, pesanan, dan riwayat pesanan. |
| `database.py` | Membuat dan mengelola database SQLite. |
| `payments.py` | Menjalankan simulasi pembayaran. |
| `validators.py` | Memvalidasi input pengguna. |
| `config.py` | Menyediakan konfigurasi aplikasi demo. |
| `test_store.py` | Berisi pengujian fungsi aplikasi. |
| `requirements.txt` | Mencatat dependensi Python. |
| `.github/workflows/devsecops.yml` | Mengatur pipeline GitHub Actions. |

**4. Cara Menjalankan Aplikasi**

**~ Persyaratan**

- Python sudah terpasang di komputer.
- Terminal atau PowerShell tersedia.

**~ Instalasi dan menjalankan aplikasi**

Buka PowerShell pada folder proyek, lalu jalankan:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Jika aktivasi virtual environment diblokir oleh PowerShell, sesuaikan kebijakan aktivasi atau gunakan interpreter Python dari environment yang sudah tersedia.

**~ Menjalankan unit test**

Untuk memeriksa fungsi aplikasi, jalankan:

```powershell
python -m pytest -v
```

**~ Menjalankan pemindaian Bandit secara lokal**

```powershell
python -m bandit -r . -x ./test_store.py,./.venv,./venv,./__pycache__
```

**~ Untuk menyimpan hasil pemindaian ke file JSON:**

```powershell
python -m bandit -r . -x ./test_store.py,./.venv,./venv,./__pycache__ -f json -o bandit-report.json
```

Bandit dapat mengembalikan kode keluar nonzero jika menemukan temuan sesuai aturan pemindaiannya. Setiap temuan perlu ditinjau sebelum menentukan tindakan perbaikan.

**5. Overview Pipeline CI/CD**

Pipeline DevSecOps diimplementasikan menggunakan GitHub Actions melalui file `.github/workflows/devsecops.yml`.

Workflow dikonfigurasi agar berjalan ketika terdapat:

- `push` ke branch `main`.
- `pull_request` yang menargetkan branch `main`.

Pipeline memiliki dua job utama:

**-> Job 1 : Build and Unit Tests**

Job ini berjalan menggunakan runner `ubuntu-latest`. Prosesnya meliputi checkout repository, menyiapkan Python, memasang dependensi, dan menjalankan unit test menggunakan pytest.

**-> Job 2 : Bandit SAST Scan**

Job ini berjalan setelah job `build` berhasil melalui konfigurasi `needs: build`. Bandit digunakan untuk memindai kode Python dan mendeteksi pola yang berpotensi menimbulkan masalah keamanan.

**-> Quality Gate**

Quality Gate diterapkan melalui aturan tingkat keparahan dan confidence temuan Bandit pada workflow. Jika hasil pemindaian memenuhi ambang yang ditetapkan, job SAST dapat gagal sehingga masalah keamanan perlu ditinjau sebelum pipeline dinyatakan berhasil.

Hasil pemindaian dapat diunggah sebagai artifact bernama `bandit-security-report` apabila langkah pembuatan laporan dan pengunggahan berhasil.

**-> Memeriksa hasil pipeline**

1. Buka repository SecureStore di GitHub.
2. Pilih tab **_Actions_**.
3. Pilih eksekusi workflow yang ingin diperiksa.
4. Periksa status job build dan Bandit SAST Scan.
5. Jika tersedia, unduh artifact laporan Bandit untuk memeriksa hasil pemindaian.

**6. Tujuan Praktikum**

Proyek SecureStore menunjukkan penerapan dasar DevSecOps dengan menggabungkan unit testing, SAST, dan Quality Gate ke dalam pipeline otomatis. Melalui praktikum ini, mahasiswa dapat mempelajari proses pengujian aplikasi, menganalisis temuan keamanan, dan memahami pentingnya pemeriksaan keamanan sebelum kode digunakan lebih lanjut.