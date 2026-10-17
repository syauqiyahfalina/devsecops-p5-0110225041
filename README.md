# SecureStore — Toko Sederhana untuk Praktikum SAST

SecureStore adalah aplikasi CLI Python untuk melihat dan mencari produk, membuat pesanan, melihat riwayat order, dan menjalankan simulasi pembayaran. Pembayaran hanya simulasi lokal, bukan integrasi gateway nyata.

> **Peringatan praktikum:** beberapa pola kode sengaja dibuat rentan untuk analisis SAST, termasuk query SQL yang dirangkai dari input, MD5 untuk referensi demo, logging referensi pembayaran, dan nilai credential palsu. Jangan gunakan untuk transaksi nyata atau production.

## Teknologi
- Python 3.12 dan SQLite
- pytest untuk unit test
- SonarQube untuk analisis statis dan Quality Gate
- GitHub Actions untuk CI

## Struktur file
- `app.py`: menu utama.
- `store.py`: daftar produk, pencarian, pembuatan pesanan, riwayat order.
- `payments.py`: simulasi pembayaran dan contoh pola tidak aman.
- `database.py`: skema SQLite dan data contoh.
- `validators.py`: validasi input.
- `config.py`: konfigurasi dan credential palsu.
- `test_store.py`: unit test.
- `sonar-project.properties`: konfigurasi SonarQube.
- `.github/workflows/devsecops.yml`: workflow CI/SAST.

## Cara menjalankan
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```
Jalankan unit test:
```bash
python -m pytest -v
```

## Overview pipeline DevSecOps
Workflow terpicu pada `push` dan `pull_request` ke branch `main` dengan runner `ubuntu-latest`.
1. `build`: memasang dependensi dan menjalankan unit test.
2. `sast-scan`: bergantung pada `build`, menjalankan SonarQube scan dan menunggu status Quality Gate.

Atur repository secrets pada **Settings → Secrets and variables → Actions**:
- `SONAR_HOST_URL`: URL server SonarQube yang bisa diakses GitHub-hosted runner.
- `SONAR_TOKEN`: token analisis SonarQube.
- `SONAR_PROJECT_KEY`: project key SonarQube.

Pipeline gagal jika scanner gagal atau Quality Gate dinyatakan gagal oleh server. Catat temuan sesuai hasil scan aktual.

## Contoh yang dianalisis dan remediasi
Contoh pola untuk dianalisis: SQL injection pada pencarian dan riwayat order, MD5 untuk referensi pembayaran, logging referensi pembayaran, dan credential palsu hard-coded. Remediasi: gunakan query berparameter, hindari MD5 untuk kebutuhan keamanan, jangan log data sensitif, dan simpan rahasia di environment/secrets.
