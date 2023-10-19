def book(judul, penulis, tersedia=True):
    return {"judul": judul, "penulis": penulis, "tersedia": tersedia}


def borrow(buku, akun):
    if buku["tersedia"]:
        buku["tersedia"] = False
        akun["pinjaman"].append(buku)
        print(f"{akun['username']} berhasil meminjam {buku['judul']}")
    else:
        print(f"{buku['judul']} sedang dipinjam oleh orang lain.")


def return_book(buku, akun):
    if buku in akun["pinjaman"]:
        buku["tersedia"] = True
        akun["pinjaman"].remove(buku)
        print(f"{akun['username']} telah mengembalikan {buku['judul']}.")
    else:
        print(f"{akun['username']} tidak memiliki buku {buku['judul']}.")


def tambah_buku(buku, admin):
    if admin["jenis_akun"] == "admin":
        admin["buku_ditambahkan"].append(buku)
        print(
            f"{admin['username']} berhasil menambahkan buku {buku['judul']} ke dalam sistem."
        )


# Inisialisasi beberapa buku
buku1 = book("Harry Potter", "J.K. Rowling")
buku2 = book("bimu", "tere liye")
buku3 = book("spors", "alkadri")

# Inisialisasi akun admin dan akun user
admin = {
    "username": "admin",
    "jenis_akun": "admin",
    "pinjaman": [],
    "buku_ditambahkan": [],
}
user = {
    "username": "user",
    "jenis_akun": "user",
    "pinjaman": [],
    "buku_ditambahkan": [],
}

# Menambahkan buku ke dalam daftar buku yang dapat dipinjam
borrowable = [buku1, buku2, buku3] + admin["buku_ditambahkan"]

while True:
    # Input pilihan sebagai admin atau user
    pilihan = input("Masukkan pilihan Anda (admin/user/exit): ").lower()

    if pilihan == "exit":
        break  # Keluar dari loop jika pengguna memasukkan "exit"

    if pilihan == "admin":
        tindakan = input(
            "Apakah Anda ingin menambah buku (tambah), meminjam buku (pinjam) atau mengembalikan(kembali)? "
        ).lower()

        if tindakan == "tambah":
            while True:
                judul_buku = input(
                    "Masukkan judul buku yang akan ditambahkan (atau ketik 'selesai' untuk selesai): "
                )
                if judul_buku.lower() == "selesai":
                    break
                penulis_buku = input("Masukkan nama penulis buku: ")
                buku_baru = book(judul_buku, penulis_buku)
                tambah_buku(buku_baru, admin)
                borrowable.append(
                    buku_baru
                )  # Menambahkan buku baru ke daftar buku yang dapat dipinjam

        elif tindakan == "pinjam":
            judul_buku = input("Masukkan judul buku yang ingin dipinjam: ")
            buku_dipinjam = None
            for buku in borrowable:
                if buku["judul"].lower() == judul_buku.lower() and buku["tersedia"]:
                    buku_dipinjam = buku
                    break
            if buku_dipinjam:
                borrow(buku_dipinjam, admin)
            else:
                print(f"Buku '{judul_buku}' tidak tersedia atau tidak ditemukan.")

        elif tindakan == "kembali":
            judul_buku = input("Masukkan judul buku yang ingin dikembalikan: ")
            buku_dikembalikan = None
            for buku in borrowable:
                if buku["judul"].lower() == judul_buku.lower():
                    buku_dikembalikan = buku
                    break
            if buku_dikembalikan:
                return_book(buku_dikembalikan, admin)
            else:
                print(
                    f"Buku '{judul_buku}' tidak ditemukan dalam daftar buku yang dapat dipinjam."
                )
        else:
            print("Pilihan tindakan tidak valid.")
    elif pilihan == "user":
        tindakan = input(
            "Apakah Anda ingin meminjam buku (pinjam) atau mengembalikan buku (kembali)? "
        ).lower()
        if tindakan == "pinjam":
            judul_buku = input("Masukkan judul buku yang ingin dipinjam: ")
            buku_dipinjam = None
            for buku in borrowable:
                if buku["judul"].lower() == judul_buku.lower() and buku["tersedia"]:
                    buku_dipinjam = buku
                    break
            if buku_dipinjam:
                borrow(buku_dipinjam, user)
            else:
                print(f"Buku '{judul_buku}' tidak tersedia atau tidak ditemukan.")
        elif tindakan == "kembali":
            judul_buku = input("Masukkan judul buku yang ingin dikembalikan: ")
            buku_dikembalikan = None
            for buku in user["pinjaman"]:
                if buku["judul"].lower() == judul_buku.lower():
                    buku_dikembalikan = buku
                    break
            if buku_dikembalikan:
                return_book(buku_dikembalikan, user)
            else:
                print(
                    f"Buku '{judul_buku}' tidak ditemukan dalam daftar peminjaman Anda."
                )
        else:
            print("Pilihan tindakan tidak valid.")
    else:
        print("Pilihan tidak valid.")

# Output status buku saat ini
print("\nStatus buku saat ini:")
for buku in borrowable:
    print(buku)
