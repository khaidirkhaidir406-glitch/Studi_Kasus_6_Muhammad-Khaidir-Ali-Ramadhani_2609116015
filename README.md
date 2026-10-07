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

**5. Fungsi ``tambah_data()``**

Digunakan untuk menambahkan data mahasiswa baru.

``input()`` digunakan untuk memasukkan nama dan NIM.

``float(input())`` digunakan untuk memasukkan nilai dalam bentuk angka, termasuk angka desimal.

``baca_data()`` digunakan untuk mengambil data yang sudah tersimpan sebelumnya.

**6. Membuat Data Baru**

data_baru merupakan dictionary yang berisi data mahasiswa.

``"Nama"`` digunakan untuk menyimpan nama mahasiswa.

``"NIM"`` digunakan untuk menyimpan nomor induk mahasiswa.

``"Nilai"`` digunakan untuk menyimpan nilai mahasiswa.

**7. Menambahkan Data**

``data.append(data_baru)`` digunakan untuk menambahkan data mahasiswa baru ke dalam daftar data.

**8. Menyimpan Data**

``open(NAMA_FILE, "w")`` digunakan untuk membuka file dengan mode "w" atau write.

``json.dump(data, f, indent=4)`` digunakan untuk menyimpan data ke dalam file JSON.

``indent=4`` digunakan agar data JSON tersusun lebih rapi dan mudah dibaca.

**9. Perulangan Menu**

``while True`` digunakan agar menu utama terus berjalan dan dapat digunakan berulang kali.

Perulangan akan berhenti ketika pengguna memilih menu **3. Keluar**.

**10. Percabangan ``if``-``elif``-``else``**

 ``if pilihan == "1"`` menjalankan fungsi ``tampilkan_data()``.
 
 ``elif pilihan == "2"`` menjalankan fungsi ``tambah_data()``.
 
 ``elif pilihan == "3"`` menghentikan program menggunakan ``break``.
 
 ``else`` digunakan untuk menampilkan pesan **"Pilihan Tidak Ada."** jika pengguna memasukkan pilihan yang tidak tersedia.

