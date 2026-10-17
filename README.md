# SecureStore — Toko Sederhana untuk Praktikum SAST

SecureStore adalah aplikasi toko sederhana berbasis Python dengan database SQLite. Aplikasi menyediakan daftar dan pencarian produk, pembuatan pesanan, riwayat pesanan, serta simulasi pembayaran.

> **Peringatan praktikum:** beberapa pola kode sengaja dibuat rentan untuk latihan analisis SAST, termasuk query SQL yang dirangkai dari input, MD5 untuk referensi demo, logging referensi pembayaran, dan nilai credential palsu. Aplikasi ini hanya untuk pembelajaran. Jangan gunakan untuk transaksi nyata atau lingkungan production.

## Teknologi yang digunakan

- **Python** untuk logika aplikasi.
- **SQLite** untuk menyimpan produk, pesanan, dan pembayaran simulasi.
- **pytest** untuk menjalankan unit test.
- **Bandit** untuk Static Application Security Testing (SAST) pada kode Python.
- **GitHub Actions** untuk menjalankan pipeline otomatis saat ada `push` atau `pull_request` ke branch `main`.

## Struktur proyek

- `app.py`: menu utama aplikasi toko.
- `store.py`: fungsi pencarian produk, pembuatan pesanan, dan riwayat pesanan.
- `database.py`: pembuatan dan pengisian database SQLite.
- `payments.py`: simulasi pembayaran.
- `validators.py`: validasi input.
- `config.py`: konfigurasi demo.
- `test_store.py`: unit test aplikasi.
- `requirements.txt`: dependensi Python.
- `.github/workflows/devsecops.yml`: workflow CI dan pemindaian Bandit.

## Cara menjalankan di Windows

Pastikan Python sudah terpasang. Dari folder proyek, jalankan:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Jika PowerShell memblokir aktivasi virtual environment, kamu dapat langsung menggunakan `python -m pip` tanpa mengaktifkannya.

## Menjalankan pengujian

```powershell
python -m pytest -v
```

## Menjalankan Bandit secara lokal

```powershell
python -m bandit -r . -x ./test_store.py,./.venv,./venv,./__pycache__
```

Untuk menghasilkan laporan JSON:

```powershell
python -m bandit -r . -x ./test_store.py,./.venv,./venv,./__pycache__ -f json -o bandit-report.json
```

Bandit dapat mengembalikan kode keluar nonzero ketika menemukan temuan sesuai aturan pemindaiannya. Itu tidak berarti file laporan gagal dibuat. Tinjau setiap temuan sebelum menentukan remediasi; Bandit tidak menjamin semua jenis kerentanan akan terdeteksi.

## Pipeline GitHub Actions

Workflow `.github/workflows/devsecops.yml` berjalan pada `push` dan `pull_request` ke branch `main`, dengan dua job:

1. `build`: memasang dependensi dan menjalankan unit test.
2. `sast-scan`: berjalan setelah `build` berhasil, memindai kode Python menggunakan Bandit, dan mencoba mengunggah `bandit-report.json` sebagai artifact.

Setelah workflow berjalan, buka tab **Actions**, pilih eksekusi workflow, lalu unduh artifact **`bandit-security-report`** pada halaman ringkasan jika proses upload berhasil. Langkah upload menggunakan `if: always()` agar tetap dicoba walaupun pemindaian gagal. Artifact tetap membutuhkan file laporan yang berhasil dibuat.

## Temuan keamanan untuk pembelajaran

Beberapa pola rentan sengaja disertakan agar dapat dianalisis. Gunakan hasil Bandit yang benar-benar muncul di eksekusi kamu sebagai bukti laporan. Jangan menganggap setiap kelemahan pasti terdeteksi oleh Bandit.
