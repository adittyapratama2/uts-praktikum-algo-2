# UTS Praktikum Algoritma & Pemrograman TA 2024/2025

Selamat datang di repository UTS Praktikum Algoritma & Pemrograman Tahun Akademik 2024/2025. Berikut adalah panduan teknis dan aturan yang harus diikuti oleh setiap mahasiswa dalam menyelesaikan ujian ini.

---

## A. Aturan Git dan Struktur Folder

1. **Fork Repository**

   - Setiap mahasiswa **wajib melakukan fork** repository ini ke akun GitHub mereka masing-masing.
   - Caranya:
     - Klik tombol **Fork** di bagian kanan atas halaman repository.
     - Repository ini akan otomatis ditambahkan ke akun GitHub Anda.

2. **Clone Repository Fork**

   - Setelah melakukan fork, clone repository yang ada di akun GitHub Anda ke komputer lokal.
   - Gunakan perintah berikut di terminal atau command prompt:
     ```bash
     git clone https://github.com/username/uts-praktikum-algo-2.git
     ```
   - Gantilah `username` dengan nama akun GitHub Anda.

3. **Buat Folder Sesuai Nama dan NIM**

   - Setelah repository ter-clone, buka folder sesuai dengan kelas Anda (misalnya, `Kelas_D`, `Kelas_E`, dsb.).
   - Di dalam folder kelas, buat folder baru dengan format:
     ```
     Nama_NIM
     ```
   - Contoh: `Kelas_E/Budi_240301001`

4. **Simpan Jawaban di Folder Masing-Masing**

   - Di dalam folder pribadi, simpan semua file kode jawaban sesuai dengan soal yang dikerjakan.
   - Setiap file jawaban **diberi nama berdasarkan nomor soal atau judul soal**. Contoh penamaan file:
     - `Soal_1.py`
     - `Soal_2.py`
     - `Soal_3.py`
   - **Catatan:** Pastikan setiap soal berada di file terpisah sesuai nomor soal.

5. **Commit dan Push Jawaban**

   - Setelah selesai mengerjakan, lakukan **commit** pada perubahan yang Anda buat.
   - Kemudian, **push** perubahan ke repository di akun GitHub Anda.
   - Contoh perintah:
     ```bash
     git add .
     git commit -m "Menambahkan jawaban UTS Praktikum"
     git push origin main
     ```

6. **Langkah-Langkah Membuat Pull Request (PR)**

   - Setelah Anda selesai mengerjakan dan menyimpan semua jawaban di repository GitHub pribadi Anda, ikuti langkah-langkah berikut untuk mengirimkan jawaban Anda melalui Pull Request (PR) ke repository utama.

   1. **Pastikan Semua Jawaban Sudah Dipush ke Repository Pribadi**

      - Setelah menyelesaikan semua soal, pastikan Anda sudah melakukan push semua file ke repository GitHub pribadi Anda.
      - Gunakan perintah berikut untuk menambahkan, commit, dan push file Anda:
        ```bash
        git add .
        git commit -m "Menyelesaikan semua soal UTS"
        git push origin main
        ```

   2. **Buka Repository Pribadi di GitHub**

      - Masuk ke akun GitHub Anda dan buka repository hasil fork dari `UTS-Praktikum-Algoritma-2024`.

   3. **Mulai Membuat Pull Request**

      - Di halaman utama repository, klik tombol **Pull Request** di bagian atas.
      - Klik tombol **New Pull Request** untuk memulai proses PR.

   4. **Pilih Repository dan Branch yang Tepat**

      - Di bagian ini, pastikan Anda membuat PR dari repository pribadi (fork) Anda menuju repository utama.
      - Sebagai contoh:
        - **Head Repository**: Pilih repository Anda sendiri (`username/UTS-Praktikum-Algoritma-2024`).
        - **Base Repository**: Pilih repository utama (`owner/UTS-Praktikum-Algoritma-2024`).
        - Pastikan branch yang dipilih adalah `main` untuk keduanya.

   5. **Isi Judul dan Deskripsi PR**

      - Beri judul PR sesuai format berikut: `PR Nama_NIM`. Contoh: `PR Budi_123456`.
      - Di bagian deskripsi, Anda bisa menambahkan catatan atau penjelasan singkat mengenai jawaban yang dikumpulkan (opsional).

   6. **Kirim Pull Request**
      - Klik **Create Pull Request** untuk mengirimkan PR ke repository utama.
      - Setelah PR berhasil dibuat, tunggu instruksi lebih lanjut atau review dari dosen/pengajar.

---

**Catatan Penting**:

- Pastikan nama folder dan file sudah sesuai dengan instruksi.
- Anda bisa mengedit PR jika ada revisi yang ingin ditambahkan sebelum disetujui oleh dosen.

---

## B. Tata Cara Mengerjakan Ujian

- Baca soal dengan cermat dan kerjakan di file yang sesuai.
- Pastikan Anda menulis **komentar** di setiap file program, mencantumkan nama, NIM, dan deskripsi singkat mengenai program tersebut.
- Gunakan **variable dan tipe data** sesuai materi yang sudah diajarkan.
- Lakukan **uji coba program** untuk memastikan kode berjalan dengan benar sebelum di-submit.

---

## C. Ketentuan dan Batas Waktu

- Ujian ini bersifat **take-home** dan harus dikerjakan secara **mandiri**.
- **Batas waktu pengumpulan**: 2024-11-14 Jam 23.00
- **Tidak diperkenankan** untuk bekerja sama atau menduplikasi jawaban dari teman.
- Keterlambatan dalam mengumpulkan jawaban akan dikenakan pengurangan nilai sesuai kebijakan yang berlaku.

---

Terima kasih, dan selamat mengerjakan UTS. Semoga sukses!
