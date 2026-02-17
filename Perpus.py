from datetime import datetime
from typing import List


# < CLASS KITAB (Encapsulation) >
# =====================================
class Kitab:
    def __init__(self, judul: str, kategori: str, stok: int):
        self.judul = judul
        self.kategori = kategori
        self.__stok = stok  # Private attribute

    @property
    def stok(self) -> int:
        return self.__stok

    def kurangi_stok(self) -> bool:
        """Mengurangi stok jika tersedia"""
        if self.__stok > 0:
            self.__stok -= 1
            return True
        return False

    def tambah_stok(self) -> None:
        """Menambah stok saat dikembalikan"""
        self.__stok += 1


# < CLASS USER (Parent Class) >
# =====================================
class User:
    def __init__(self, nama: str):
        self.nama = nama


# < INHERITANCE >
# =====================================
class Admin(User):
    pass


class Santri(User):
    pass



# < CLASS PERPUSTAKAAN >
# =====================================
class Perpustakaan:
    def __init__(self):
        self.daftar_kitab: List[Kitab] = []
        self.data_peminjaman: List[tuple] = []

    def tambah_kitab(self, kitab: Kitab) -> None:
        self.daftar_kitab.append(kitab)

    def tampilkan_semua_kitab(self) -> None:
        if not self.daftar_kitab:
            print("📚 Belum ada kitab dalam perpustakaan.")
            return

        print("\n=== DAFTAR KITAB ===")
        for index, kitab in enumerate(self.daftar_kitab, start=1):
            print(f"{index}. {kitab.judul} | Kategori: {kitab.kategori} | Stok: {kitab.stok}")

    def pinjam_kitab(self, nama_santri: str, judul: str) -> None:
        for kitab in self.daftar_kitab:
            if kitab.judul.lower() == judul.lower():
                if kitab.kurangi_stok():
                    tanggal = datetime.now().strftime("%d-%m-%Y")
                    self.data_peminjaman.append((nama_santri, judul, tanggal))
                    print("✅ Peminjaman berhasil dicatat.")
                else:
                    print("❌ Stok habis! Tidak bisa dipinjam.")
                return
        print("❌ Kitab tidak ditemukan.")

    def kembalikan_kitab(self, judul: str) -> None:
        for kitab in self.daftar_kitab:
            if kitab.judul.lower() == judul.lower():
                kitab.tambah_stok()
                print("✅ Kitab berhasil dikembalikan.")
                return
        print("❌ Kitab tidak ditemukan.")

    def tampilkan_riwayat(self) -> None:
        if not self.data_peminjaman:
            print("📭 Belum ada riwayat peminjaman.")
            return

        print("\n=== 📜 RIWAYAT PEMINJAMAN ===")
        for index, data in enumerate(self.data_peminjaman, start=1):
            nama, judul, tanggal = data
            print(f"{index}. {nama} meminjam '{judul}' pada {tanggal}")


# < PROGRAM UTAMA (CLI) >
# =====================================
def main():
    perpustakaan = Perpustakaan()

    # Data awal kitab
    perpustakaan.tambah_kitab(Kitab("Fathul Qorib", "Fiqh", 3))
    perpustakaan.tambah_kitab(Kitab("'Aqidatuna", "Aqidah", 3))
    perpustakaan.tambah_kitab(Kitab("Arbain Nawawi", "Hadits", 3))
    perpustakaan.tambah_kitab(Kitab("Al-Ajurumiyah", "Nahwu", 3))
    perpustakaan.tambah_kitab(Kitab("Aby", "Bahasa Arab", 3))
    perpustakaan.tambah_kitab(Kitab("Fathul 'Aliy", "Fiqh", 3))
    perpustakaan.tambah_kitab(Kitab("Riyadhus Shalihin", "Hadist", 3))

    
    

    while True:
        print("\n=== 📚 PERPUSTAKAAN KITAB ===")
        print("1. Tampilkan Semua Kitab")
        print("2. Pinjam Kitab")
        print("3. Kembalikan Kitab")
        print("4. Riwayat Peminjaman")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            perpustakaan.tampilkan_semua_kitab()

        elif pilihan == "2":
            nama = input("Nama Santri: ")
            judul = input("Judul Kitab: ")
            perpustakaan.pinjam_kitab(nama, judul)

        elif pilihan == "3":
            judul = input("Judul Kitab: ")
            perpustakaan.kembalikan_kitab(judul)

        elif pilihan == "4":
            perpustakaan.tampilkan_riwayat()

        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem 📚")
            break

        else:
            print("❌ Pilihan tidak valid! Masukkan angka 1-5.")


if __name__ == "__main__":
    main()
