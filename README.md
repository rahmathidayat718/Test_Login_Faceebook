# Automation Testing untuk Website Facebook

## Deskripsi Proyek

Proyek ini adalah suite **automation testing** untuk memverifikasi halaman login Facebook dan menguji fungsionalitas login dengan data yang valid menggunakan **Selenium** dan **Python**. Pengujian ini menggunakan framework **pytest**, dan hasilnya disajikan dalam bentuk laporan **HTML** yang mudah dibaca.

### Fitur yang Diuji:
1. **Verifikasi Halaman Login Facebook**  
   Memastikan elemen pada halaman login tersedia dan berfungsi dengan baik.
2. **Login dengan Data yang Valid**  
   Menguji kemampuan login menggunakan kredensial yang benar.  
   > **Catatan:** Login valid akan gagal jika muncul verifikasi kode melalui email, karena pengujian ini belum mendukung pengambilan kode otomatis.

---

## Tools & Teknologi
- **Python**: Bahasa pemrograman untuk menulis skrip pengujian.
- **Selenium**: Untuk otomatisasi browser dan interaksi dengan elemen web.
- **pytest**: Framework untuk menyusun dan menjalankan pengujian.
- **pytest-html**: Plugin untuk menghasilkan laporan pengujian dalam format HTML.

---

---

## Instalasi

1. Clone repository:
   ```bash
   git clone https://github.com/username/facebook-automation.git
   cd facebook-automation
