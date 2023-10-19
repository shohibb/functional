expenses = [
    {"tanggal": "2023-07-25", "deskripsi": "Makan Siang", "jumlah": 50000},
    {"tanggal": "2023-07-25", "deskripsi": "Transportasi", "jumlah": 25000},
    {"tanggal": "2023-07-26", "deskripsi": "Belanja", "jumlah": 100000},
]


# Fungsi pure untuk menambahkan pengeluaran
def add_expense(date, description, amount, expense_list):
    return expense_list + [
        {"tanggal": date, "deskripsi": description, "jumlah": amount}
    ]


# Fungsi pure untuk menghitung total pengeluaran
calculate_total_expenses = lambda expenses: sum(
    expense["jumlah"] for expense in expenses
)


# Fungsi pure untuk mendapatkan pengeluaran berdasarkan tanggal
def get_expenses_by_date(expense_list, target_date):
    return [expense for expense in expense_list if expense["tanggal"] == target_date]


# Fungsi pure untuk menghasilkan laporan pengeluaran harian
def generate_expenses_report(expense_list):
    daily_expenses = {}

    for expense in expense_list:
        date = expense["tanggal"]
        if date in daily_expenses:
            daily_expenses[date].append(expense)
        else:
            daily_expenses[date] = [expense]

    return (
        f"{date} - Total Pengeluaran: Rp {sum(expense['jumlah'] for expense in expenses)}"
        for date, expenses in daily_expenses.items()
    )


# Fungsi pure untuk menambah pengeluaran interaktif
def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    print("Pengeluaran berhasil ditambahkan.")
    return add_expense(date, description, amount, expenses)


# Fungsi pure untuk melihat pengeluaran berdasarkan tanggal
def view_expenses_by_date(expenses):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(expenses, date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")


# Fungsi pure untuk melihat laporan pengeluaran harian
def view_expenses_report(expenses):
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report(expenses)
    for entry in expenses_report:
        print(entry)


# Fungsi pure untuk mendapatkan input pengguna
get_user_input = lambda command: int(input(command))


# Fungsi pure untuk menampilkan menu
def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")


def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")


if __name__ == "__main__":
    main()
expenses = [
    {"tanggal": "2023-07-25", "deskripsi": "Makan Siang", "jumlah": 50000},
    {"tanggal": "2023-07-25", "deskripsi": "Transportasi", "jumlah": 25000},
    {"tanggal": "2023-07-26", "deskripsi": "Belanja", "jumlah": 100000},
]

# TODO 1 Buatlah Fungsi add_expense disini


def add_expense(date, description, amount):
    global expenses  # Gunakan variabel global
    add = expenses.append({"tanggal": date, "deskripsi": description, "jumlah": amount})
    return add  # Kembalikan daftar expenses


# TODO 2 Buatlah fungsi calculate_total_expenses disini

calculate_total_expenses = lambda expenses: sum(
    expense["jumlah"] for expense in expenses
)

# TODO 3 Buatlah fungsi get_expenses_ by_date disini


def get_expenses_by_date(expense_list, target_date):
    return [expense for expense in expense_list if expense["tanggal"] == target_date]


# TODO 4 Buatlah fungsi generate_expenses_report disini


def generate_expenses_report(expense_list):
    daily_expenses = {}

    for expense in expense_list:
        date = expense["tanggal"]
        if date in daily_expenses:
            daily_expenses[date].append(expense)
        else:
            daily_expenses[date] = [expense]

    for date, expenses in daily_expenses.items():
        total_expense = sum(expense["jumlah"] for expense in expenses)
        yield f"{date} - Total Pengeluaran: Rp {total_expense}"


# TODO 5 pastikan semua fungsi yang ada sudah berupa pure function
# jika belum, maka modifikasilah


def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    new_expenses = add_expense(date, description, amount)
    print("Pengeluaran berhasil ditambahkan.")
    return new_expenses


def view_expenses_by_date(expenses):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(expenses, date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")


def view_expenses_report(expenses):
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report(expenses)
    for entry in expenses_report:
        print(entry)


def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")


# TODO 6 ubah fungsi berikut ke dalam bentuk lambda
def get_user_input(command):
    return int(input(command))


def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")


if __name__ == "__main__":
    main()
