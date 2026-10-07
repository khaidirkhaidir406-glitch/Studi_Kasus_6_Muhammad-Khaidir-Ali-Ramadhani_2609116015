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



 # DOKUMENTASI OUTPUT PROGRAM

 <img width="317" height="238" alt="Screenshot 2026-10-08 011445" src="https://github.com/user-attachments/assets/01c50f7b-c484-450d-8762-4cdb0e9fdf7d" />

 ini adalah contoh output program menambah data.


 <img width="383" height="362" alt="Screenshot 2026-10-08 011452" src="https://github.com/user-attachments/assets/49fd195a-43ed-4083-9a6f-f6f670d01ebc" />

 ini adalah contoh output program menampilkan data.


 <img width="321" height="176" alt="Screenshot 2026-10-08 011457" src="https://github.com/user-attachments/assets/c5f97ec2-b147-48f0-a50c-cdb45d86e0cd" />

 ini adalah contoh output program untuk mengakhiri program.


 <img width="396" height="528" alt="Screenshot 2026-10-08 011524" src="https://github.com/user-attachments/assets/decdf9e7-6979-4fa6-ac6a-d8d0559739a4" />

 ini adalah output program ketika program di run ulang (tetap menampilkan data yang sudah tersimpan sebelumnya).





