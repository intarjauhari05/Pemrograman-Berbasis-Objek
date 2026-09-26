# Jawaban Teori Latihan Bab 3: Eksepsi

---

### Soal 1:
**Mengapa sebuah program perlu memiliki mekanisme penanganan error? Jelaskan dampaknya jika error tidak ditangani dengan baik!**

**Jawaban:**
1. **Pentingnya Mekanisme Penanganan Error:**
   - **Mencegah Program Crash (Abrupt Termination):** Penanganan error memungkinkan program tetap berjalan meskipun terjadi kesalahan tak terduga (*runtime error*), alih-alih langsung terhenti secara tiba-tiba.
   - **Meningkatkan User Experience (UX):** Memberikan pesan kesalahan yang informatif, ramah, dan mudah dipahami oleh pengguna umum, bukan sekadar *traceback* kode yang membingungkan.
   - **Manajemen Sumber Daya (Resource Management):** Memastikan proses pembersihan (*cleanup*) seperti menutup koneksi database, file, atau koneksi jaringan tetap terlaksana meskipun terjadi kegagalan sistem.
   - **Integritas dan Keamanan Data:** Mencegah terjadinya korupsi data atau inkonsistensi data saat terjadi error di tengah-tengah transaksi (misalnya proses transfer/penarikan dana).

2. **Dampak Jika Error Tidak Ditangani dengan Baik:**
   - Program akan langsung berhenti (*crash*) di tengah jalan saat menghadapi input tidak valid atau kegagalan sistem.
   - Terjadinya kebocoran data sensitif (*data exposure*) atau celah keamanan karena *traceback error* teknis dapat menampilkan struktur direktori, query database, atau kode internal kepada pengguna luar.
   - Kehilangan data (*data loss*) atau transaksi yang menggantung akibat file/koneksi tidak tertutup dengan benar.
   - Menurunkan kepercayaan pengguna terhadap kestabilan dan keandalan aplikasi.

---

### Soal 2:
**Jelaskan keuntungan penggunaan *custom exception* dibandingkan hanya menggunakan *exception* bawaan Python!**

**Jawaban:**
Keuntungan penggunaan *custom exception* (eksepsi buatan sendiri) antara lain:
1. **Kejelasan Konteks Bisnis (Domain-Specific Context):** Memberikan nama error yang merefleksikan logika bisnis aplikasi secara spesifik (misal: `SaldoTidakCukupError`, `AkunTerkunciError`) daripada sekadar menggunakan error generik seperti `ValueError` atau `Exception`.
2. **Penanganan Error yang Lebih Presisi (Granular Error Handling):** Memungkinkan kita menangkap (*catch*) kesalahan spesifik tersebut secara terpisah pada blok `except` tanpa risiko salah menangkap error bawaan Python lainnya yang tidak berhubungan.
3. **Penyampaian Pesan dan Data Tambahan:** Custom exception dapat ditambahkan atribut/properti khusus (misalnya menyimpan sisa saldo, kode error internal, ID transaksi) untuk mempermudah debugging dan logging.
4. **Meningkatkan Keterbacaan dan Kerapian Kode (*Clean Code*):** Kode menjadi lebih mudah dibaca dan dipelihara (*maintainable*) oleh tim pengembang karena aliran penanganan kesalahan terstruktur rapi.

---

### Soal 3:
**Jelaskan cara kerja blok `try`, `except`, dan `finally` dalam penanganan error pada Python!**

**Jawaban:**
1. **Blok `try`:**
   - Berisi baris kode yang berpotensi menghasilkan kesalahan (*runtime exception*).
   - Python akan mengeksekusi kode di dalam blok ini baris demi baris. Jika tidak ada error, seluruh blok dieksekusi normal dan blok `except` akan dilewati.
   - Jika terjadi error pada salah satu baris, eksekusi kode di dalam `try` langsung berhenti pada titik tersebut dan Python beralih mencari blok `except` yang sesuai.

2. **Blok `except`:**
   - Berisi kode yang akan dijalankan **hanya jika** terjadi eksepsi pada blok `try`.
   - Dapat menangkap tipe exception tertentu (misal `except ValueError:`) atau bertingkat (*multiple except*).
   - Menghindari penghentian program dengan menyediakan aksi alternatif/solusi (misal mencatat log, menampilkan pesan error, memberi nilai default).

3. **Blok `finally`:**
   - Berisi kode yang **pasti akan selalu dieksekusi**, baik saat blok `try` berhasil tanpa error, maupun saat terjadi error dan ditangkap oleh `except`, bahkan jika ada pernyataan `return` atau error yang tidak tertangkap.
   - Umumnya digunakan untuk proses pembersihan (*cleanup*), seperti menutup file yang dibuka (`file.close()`), memutus koneksi database, atau melepas *lock* sumber daya sistem.

**Alur Eksekusi Singkat:**
- *Tidak ada error:* `try` ➔ `finally`
- *Ada error & tertangkap:* `try` (berhenti di baris error) ➔ `except` ➔ `finally`
- *Ada error & tidak tertangkap:* `try` ➔ `finally` ➔ Program terhenti/melempar unhandled exception.
