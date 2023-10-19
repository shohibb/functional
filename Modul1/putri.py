# Inisialisasi daftar buku 
daftar_buku = []


# Fungsi tambah buku
def tambah_buku():
    judul = input("Judul buku: ")
    kode = input("Kode buku: ")
    stok = int(input("Jumlah yang tersedia: "))
    buku = {"Judul": judul, "Kode buku": kode, "Stok": stok}
    daftar_buku.append(buku)
    print(f"Buku '{judul}' dengan kode '{kode}' berhasil ditambahkan ke daftar.\n")


# Fungsi pinjam buku
def pinjam_buku():
    judul = input("Judul Buku: ")
    buku_ditemukan = False  # Inisialisasi variabel buku_ditemukan
    for buku in daftar_buku:
        if buku["Judul"] == judul:
            buku_ditemukan = True
            if buku["Stok"] > 0:
                buku["Stok"] -= 1
                print(f"Buku '{judul}' Sudah Terambil.")
            else:
                print(f"Buku '{judul}' tidak tersedia saat ini.")
            break
    if not buku_ditemukan:
        print(f"Buku '{judul}' tidak ditemukan di perpustakaan.")


# Fungsi kembalikan buku
def kembalikan_buku():
    judul = input("Judul Buku: ")
    buku_ditemukan = False  # Inisialisasi variabel buku_ditemukan
    for buku in daftar_buku:
        if buku["Judul"] == judul:
            buku_ditemukan = True
            buku["Stok"] += 1
            print(f"Terima kasih sudah mengembalikan buku '{judul}'.")
            return
    if not buku_ditemukan:
        print(f"Anda belum meminjam buku '{judul}'.")


# Fungsi menampilkan semua buku
def tampilkan_semua_buku():
    if len(daftar_buku) > 0:
        print("\nDaftar Buku:")
        for buku in daftar_buku:
            print(
                f"Judul: {buku['Judul']}, Kode buku: {buku['Kode buku']}, Stok: {buku['Stok']}"
            )
    else:
        print("\nPerpustakaan kosong.")


# Fungsi login admin
def login_admin():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")
    return username == "admin" and password == "ADM"


# Fungsi login user
def login_user():
    username = input("Masukkan username user: ")
    password = input("Masukkan password user: ")
    return username == "user" and password == "USR"


while True:
    print("\nSelamat Datang di Perpustakaan\n")
    print("Menu:")
    print("1. Admin")
    print("2. User")
    print("3. Keluar")

    pilihan_menu = input("Pilih menu (1/2/3): ")

    # while pilihan_menu != '3':  # Loop utama
    if pilihan_menu == "1":
        if login_admin():
            while True:
                print("\nMenu Admin:")
                print("1. Tambah Buku")
                print("2. Tampilkan Semua Buku")
                print("3. Keluar")
                admin_menu = input("Pilih menu admin (1/2/3): ")
                if admin_menu == "1":
                    tambah_buku()
                elif admin_menu == "2":
                    tampilkan_semua_buku()
                elif admin_menu == "3":
                    break  # Keluar dari menu admin
                else:
                    print("Pilihan admin tidak valid.")
        else:
            print("Login admin salah.")
    elif pilihan_menu == "2":
        if login_user():
            while True:
                print("\nMenu User:")
                print("1. Tampilkan Semua Buku")
                print("2. Pinjam Buku")
                print("3. Kembalikan Buku")
                print("4. Keluar")
                user_menu = input("Pilih menu user (1/2/3/4): ")
                if user_menu == "1":
                    tampilkan_semua_buku()
                elif user_menu == "2":
                    pinjam_buku()
                elif user_menu == "3":
                    kembalikan_buku()
                elif user_menu == "4":
                    break
                else:
                    print("Pilihan user tidak valid.")
        else:
            print("Login user salah.")
    elif pilihan_menu == "3":
        print("Terima kasih telah menggunakan perpustakaan. Sampai jumpa!")
        break
    # else:
    #     print("Terima kasih telah menggunakan perpus")
    # Setelah keluar dari menu admin atau user, kembali ke menu utama
