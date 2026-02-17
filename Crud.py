from prettytable import PrettyTable

# List untuk menyimpan data siswa
data = []

# ===============================
# FUNGSI TAMBAH DATA
# ===============================
def tambah_data():
    print("\n=== Tambah Data ===")
    id = int(input("Masukkan ID: "))
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")

    data.append({
        "id": id,
        "nama": nama,
        "kelas": kelas
    })

    print("✅ Data berhasil ditambahkan!")


# ===============================
# FUNGSI TAMPIL DATA
# ===============================
def tampil_data():
    print("\n=== Daftar Data ===")

    if len(data) == 0:
        print("❌ Data masih kosong")
        return

    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Kelas"]

    for d in data:
        table.add_row([d["id"], d["nama"], d["kelas"]])

    print(table)


# ===============================
# FUNGSI UBAH DATA
# ===============================
def ubah_data():
    print("\n=== Ubah Data ===")
    id_cari = int(input("Masukkan ID yang ingin diubah: "))

    for d in data:
        if d["id"] == id_cari:
            d["nama"] = input("Masukkan Nama Baru: ")
            d["kelas"] = input("Masukkan Kelas Baru: ")
            print("✅ Data berhasil diubah!")
            return

    print("❌ Data tidak ditemukan")


# ===============================
# FUNGSI HAPUS DATA
# ===============================
def hapus_data():
    print("\n=== Hapus Data ===")
    id_cari = int(input("Masukkan ID yang ingin dihapus: "))

    for d in data:
        if d["id"] == id_cari:
            data.remove(d)
            print("✅ Data berhasil dihapus!")
            return

    print("❌ Data tidak ditemukan")


# ===============================
# MENU UTAMA
# ===============================
while True:
    print("\n=== MENU ===")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampil_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "0":
        print("👋 Program selesai, terima kasih!")
        break
    else:
        print("❌ Pilihan tidak valid")
