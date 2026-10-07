# Studi_Kasus_6_Muhammad-Khaidir-Ali-Ramadhani_2609116015

**Nama : Muhammad Khaidir Ali Ramadhani**

**NIM : 2609116015**

**Kelas : A**

# Penjelasan Kode Program

**1. Import Library**

``Import json`` : digunakan untuk membaca dan menyimpan data dalam format JSON.

``Import os`` : digunakan untuk mengecek apakah file ``data_nilai.json`` sudah tersedia atau belum.

**2. Menentukkan Nama File**

``NAMA_FILE = "data_nilai.json"`` : digunakan untuk menentukan nama file yang menjadi tempat penyimpanan data nilai mahasiswa.

**3. Fungsi ``baca_data()``**

Digunakan untuk membaca data mahasiswa yang tersimpan di file JSON.

``os.path.exists(NAMA_FILE)`` digunakan untuk mengecek apakah file sudah ada.

Jika file belum ada, program mengembalikan data kosong dengan ``return []``.

``open(NAMA_FILE, "r")`` digunakan untuk membuka file dengan mode ``"r"`` atau *read*.

``json.load(f)`` digunakan untuk membaca dan mengubah data JSON menjadi data Python.

**4. Fungsi ``tampilkan_data()``**

Digunakan untuk menampilkan data nilai mahasiswa yang sudah tersimpan.

Fungsi ``baca_data()`` dipanggil untuk mengambil data dari file.

``len(data) == 0`` digunakan untuk mengecek apakah data masih kosong.

Jika tidak ada data, program menampilkan pesan **"Belum ada data nilai."**

Jika terdapat data, perulangan ``for`` digunakan untuk menampilkan **Nama**, **NIM**, dan **Nilai** setiap mahasiswa.



