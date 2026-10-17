### Security Analysis (SAST)

Proyek SecureStore menggunakan **Bandit** untuk melakukan Static Application Security Testing (SAST) pada kode Python. Bandit memeriksa pola kode yang berpotensi menimbulkan masalah keamanan.

Pemindaian dijalankan secara otomatis melalui GitHub Actions setelah ada push atau pull request ke branch `main`. Hasil pemindaian dapat diunduh melalui artifact pada workflow GitHub Actions.

Tools yang digunakan:
- Python sebagai bahasa pemrograman.
- SQLite sebagai database.
- pytest untuk pengujian aplikasi.
- Bandit untuk analisis keamanan kode.
- GitHub Actions untuk otomatisasi pipeline CI/CD.