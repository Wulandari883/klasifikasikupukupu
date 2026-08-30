# Analisis Alur Kerja Sistem: Activity Diagram Klasifikasi Spesies Kupu-Kupu (Updated)

Dokumen ini berisi narasi formal untuk **Activity Diagram Klasifikasi Spesies Kupu-Kupu** dengan menggunakan pendekatan **3 swimlane** (Pengguna, Sistem, Database) yang telah diperbarui sesuai dengan alur logika antarmuka aplikasi. Narasi ini disusun dengan menggunakan terminologi akademis dan bahasa Indonesia baku (EYD) yang siap disalin langsung ke dalam naskah **Bab III (Analisis dan Perancangan Sistem)** skripsi S1 Informatika Anda.

---

## 1. Deskripsi Umum
Activity Diagram Klasifikasi memodelkan alur proses transaksi pengunggahan citra kupu-kupu secara dinamis serta pengolahan hasilnya di antarmuka sistem. Alur diagram ini disusun secara vertikal untuk menggambarkan bagaimana sistem melakukan prapemrosesan citra, menjalankan model deep learning *EfficientNet-B0*, mengevaluasi batas keyakinan model (*confidence threshold*), mengambil informasi detail taksonomi spesies, menyimpan data riwayat transaksional, mengambil data riwayat klasifikasi terbaru (*Prediction History*), serta merender luaran hasil akhir secara bersyarat.

Diagram ini dibagi menjadi **3 swimlane** utama untuk menggambarkan kolaborasi dan pembagian tanggung jawab fungsional dalam sistem:
1. **Pengguna**: Aktor manusia yang berinteraksi langsung dengan antarmuka aplikasi Lepidoptera Archive.
2. **Sistem**: Subsistem perangkat lunak (konsolidasi Next.js Frontend, FastAPI Backend, dan Model AI) yang memproses logika validasi, pemrosesan citra digital, inferensi neural network, pemanggilan kueri database, serta pengaturan tampilan visual.
3. **Database**: Repositori database relasional (Supabase) yang menyimpan data taksonomi dan melakukan operasi penyimpanan dan pembacaan transaksional.

---

## 2. Identifikasi Entitas (Swimlane)

| No | Nama Swimlane | Peran dan Tanggung Jawab dalam Sistem |
| :--- | :--- | :--- |
| 1 | **Pengguna** | Memulai aktivitas, memilih berkas citra, melakukan aksi unggah berkas, dan melihat hasil presentasi klasifikasi akhir secara visual. |
| 2 | **Sistem** | Memvalidasi file gambar, melakukan pra-pemrosesan citra digital, menjalankan inferensi model AI, mengevaluasi nilai ambang batas keyakinan (*confidence threshold*), mengoordinasikan transaksi baca/tulis ke database, serta menampilkan komponen hasil dan *Prediction History* secara dinamis. |
| 3 | **Database** | Menyediakan informasi detail taksonomi spesies, memproses penulisan data transaksional ke tabel `riwayat_klasifikasi` dan `kandidat_klasifikasi`, serta mengembalikan koleksi riwayat klasifikasi terbaru. |

---

## 3. Narasi Alur Aktivitas (Step-by-Step)

Rincian alur aktivitas klasifikasi spesies kupu-kupu digambarkan sebagai berikut:

1. **Mulai**: Alur aktivitas dimulai pada *Initial Node* di kolom **Pengguna**.
2. **Pengguna** membuka menu *Classification* pada antarmuka aplikasi.
3. **Pengguna** memilih gambar kupu-kupu dari penyimpanan lokal perangkat atau melalui kamera.
4. **Pengguna** mengunggah berkas gambar tersebut ke dalam sistem.
5. **Sistem** mendeteksi unggahan gambar dan melakukan **Validasi File Gambar** secara lokal (memeriksa format file JPG/PNG/WEBP serta ukuran file maksimum 5 MB).
6. Pada *Decision Node* **Apakah file valid?**:
   - **TIDAK VALID**: Jika berkas citra tidak lolos kriteria validasi, **Sistem** mengeksekusi aktivitas **Menampilkan Pesan Error** pada layar antarmuka pengguna, lalu mengembalikan alur secara melingkar (*loop back*) ke aktivitas **Mengunggah Gambar**.
   - **VALID**: Jika berkas citra lolos kriteria validasi, alur berlanjut ke aktivitas **Preprocessing Citra**.
7. **Sistem** melakukan pra-pemrosesan citra digital meliputi penskalaan dimensi (*resize*) ke resolusi standar $224 \times 224$ piksel serta **Normalisasi** nilai intensitas warna piksel citra ke dalam rentang [0, 1].
8. **Sistem** melanjutkan dengan aktivitas **Menjalankan Model EfficientNet-B0** untuk melakukan inferensi (*forward propagation*).
9. **Sistem** memproses hasil keluaran model dan menjalankan aktivitas **Menghasilkan Prediksi (Spesies &amp; Confidence Score)**.
10. Pada *Decision Node* **Apakah Confidence Score &ge; 65%?**:

    ### A. Alur Sukses (Cabang YA):
    1. **Sistem mengambil detail spesies dari database** berdasarkan ID spesies terdeteksi utama.
    2. **Database mengirim detail spesies** (nama umum/spesies, nama ilmiah, deskripsi, dll.) kembali ke Sistem.
    3. **Sistem menyimpan hasil ke tabel riwayat_klasifikasi** untuk mencatat transaksi klasifikasi.
    4. **Database menyimpan data riwayat** secara fisik ke penyimpanan.
    5. **Sistem menyimpan kandidat prediksi ke tabel kandidat_klasifikasi** untuk alternatif prediksi.
    6. **Database menyimpan kandidat prediksi** ke penyimpanan.
    7. **Sistem mengambil data riwayat klasifikasi terbaru** (*Prediction History*).
    8. **Database mengirim data riwayat** yang terbaru ke Sistem.
    9. **Sistem menampilkan: Nama spesies, Nama ilmiah, Confidence Score, dan Prediction History** pada antarmuka visual.
    10. **Pengguna melihat hasil klasifikasi** pada layar, dan alur aktivitas selesai pada *Final Node*.

    ### B. Alur Gagal (Cabang TIDAK):
    1. **Sistem menampilkan pesan: "Gagal Dideteksi"** pada layar antarmuka pengguna.
    2. **Sistem tidak mengambil detail spesies**, tidak menyimpan riwayat klasifikasi, dan tidak menyimpan kandidat prediksi ke database.
    3. **Pengguna melihat pesan gagal dideteksi** pada antarmuka visual, dan alur aktivitas selesai pada *Final Node*.

---

## 4. Spesifikasi Simbol UML Activity Diagram

| Simbol | Bentuk Visual | Deskripsi Fungsi |
| :---: | :---: | :--- |
| **Initial Node** | Lingkaran Hitam Solid | Titik awal dimulainya alur aktivitas klasifikasi spesies oleh Pengguna. |
| **Action State** | Persegi Panjang Sudut Tumpul (*Rounded Rectangle*) | Unit kerja/proses komputasi yang dieksekusi oleh entitas dalam swimlane bersangkutan (misalnya: *Preprocessing Citra*, *Menyimpan Data*). |
| **Decision Node** | Belah Ketupat (*Rhombus*) | Titik percabangan kondisi logis (mengevaluasi validitas berkas citra dan ambang batas *confidence score*). |
| **Control Flow** | Garis Berpanah Solid | Mengarahkan urutan transisi eksekusi dari satu aktivitas ke aktivitas berikutnya. |
| **Swimlane** | Kolom Vertikal Terpartisi | Memisahkan pembagian tanggung jawab fungsional (Pengguna, Sistem, Database). |
| **Final Node** | Lingkaran Hitam Berbingkai | Titik akhir berhentinya seluruh proses klasifikasi pada sistem setelah hasil ditampilkan kepada Pengguna. |
