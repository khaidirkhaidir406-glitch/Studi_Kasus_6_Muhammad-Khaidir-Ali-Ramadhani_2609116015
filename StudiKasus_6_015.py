import json
import os

NAMA_FILE = "data_nilai.json"

def baca_data():
    if not os.path.exists(NAMA_FILE):
        return []
    with open(NAMA_FILE, "r") as f:
        data = json.load(f)
        return data
    return []

def tampilkan_data():
    data = baca_data()

    print("=" * 30)
    print("        DATA NILAI MAHASISWA        ")
    print("=" * 30)

    if len(data) == 0:
        print("Belum ada data nilai.")
    else:
        for mahasiswa in data:
            print("NAMA  :", mahasiswa["Nama"])
            print("NIM   :", mahasiswa["NIM"])
            print("NILAI :", mahasiswa["Nilai"])
    print("--------------------------------------------")

def tambah_data():
    nama = input("Masukkan Nama         : ")
    nim = input("Masukkan NIM           : ")
    nilai = float(input("Masukkan Nilai : "))

    data = baca_data()

    data_baru = {
        "Nama" : nama,
        "NIM" : nim,
        "Nilai" : nilai
    }

    data.append(data_baru)
    with open(NAMA_FILE, "w") as f:
        json.dump(data, f, indent = 4)
    print("\n Data berhasil ditambahkan^^")

while True: 
    print("=" * 30)
    print("SISTEM PENCATATAN NILAI MAHASISWA    ")
    print("=" * 30)
    print("1. Tampilkan Data Nilai")
    print("2. Tambah Data Nilai")
    print("3. Keluar")

    pilihan = input("Pilih Menu : ")
    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        print("Program selesai.")
        break 
    else: 
        print("Pilihan Tidak Ada.")