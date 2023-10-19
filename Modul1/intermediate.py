def tambah_peserta(data_peserta):
    nama = input("Masukkan nama peserta: ")
    nilai = int(input("Masukkan nilai peserta: "))
    id_peserta = len(data_peserta)
    hasil_akhir = "Lolos" if nilai >= 75 else "Tidak Lolos"
    peserta = (id_peserta, nama, nilai, hasil_akhir)
    data_peserta.append(peserta)
    print(f"Data peserta {nama} berhasil ditambahkan.")


def tampilkan_data_peserta(data_peserta, peran):
    if not data_peserta:
        print("Belum ada data peserta.")
    else:
        print("\nData Peserta:")
        if peran == "admin":
            for peserta in data_peserta:
                id_peserta, nama, nilai, hasil_akhir = peserta
                print(
                    f"ID: {id_peserta}, Nama: {nama}, Nilai: {nilai}, Hasil Akhir: {hasil_akhir}"
                )
        elif peran == "peserta":
            id_peserta = int(input("Masukkan ID peserta Anda: "))
            if 0 <= id_peserta < len(data_peserta):
                peserta = data_peserta[id_peserta]
                id_peserta, nama, nilai, hasil_akhir = peserta
                print(
                    f"ID: {id_peserta}, Nama: {nama}, Nilai: {nilai}, Hasil Akhir: {hasil_akhir}"
                )
            else:
                print("ID peserta tidak valid.")


def edit_nilai(data_peserta):
    if not data_peserta:
        print("Belum ada data peserta.")
        return
    id_peserta = int(input("Masukkan ID peserta yang akan diubah nilainya: "))
    if 0 <= id_peserta < len(data_peserta):
        nilai = int(input("Masukkan nilai baru: "))
        hasil_akhir = "Lolos" if nilai >= 75 else "Tidak Lolos"
        data_peserta[id_peserta] = (
            id_peserta,
            data_peserta[id_peserta][1],
            nilai,
            hasil_akhir,
        )
        print(f"Nilai peserta {data_peserta[id_peserta][1]} berhasil diubah.")


def login():
    while True:
        print("\nPilihan Masuk:")
        print("1. Masuk sebagai Admin")
        print("2. Masuk sebagai Peserta")
        print("3. Keluar")
        pilihan = input("Masukkan nomor pilihan: ")

        if pilihan == "1":
            return "admin"
        elif pilihan == "2":
            return "peserta"
        elif pilihan == "3":
            return "keluar"
        else:
            print("Pilihan tidak valid.")


# Inisialisasi data peserta
data_peserta = []

while True:
    peran = login()

    if peran == "admin":
        while True:
            print("\nPilihan Admin:")
            print("1. Tambah Peserta")
            print("2. Tampilkan Data Peserta")
            print("3. Edit Nilai Peserta")
            print("4. Kembali")
            admin_pilihan = input("Masukkan nomor pilihan: ")

            if admin_pilihan == "1":
                tambah_peserta(data_peserta)
            elif admin_pilihan == "2":
                tampilkan_data_peserta(data_peserta, peran)
            elif admin_pilihan == "3":
                edit_nilai(data_peserta)
            elif admin_pilihan == "4":
                break
            else:
                print("Pilihan tidak valid.")
    elif peran == "peserta":
        print("\nSelamat datang, Peserta.")
        tampilkan_data_peserta(data_peserta, peran)
    elif peran == "keluar":
        print("Terima kasih. Sampai jumpa!")
        break
