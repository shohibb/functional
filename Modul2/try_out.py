expenses = [
    {"tanggal": "2023-07-25", "deskripsi": "Makan Siang", "jumlah": 50000},
    {"tanggal": "2023-07-25", "deskripsi": "Transportasi", "jumlah": 25000},
    {"tanggal": "2023-07-26", "deskripsi": "Belanja", "jumlah": 100000},
]


def add_expense(date, description, amount):
    global expenses  # Gunakan variabel global
    expenses.append({"tanggal": date, "deskripsi": description, "jumlah": amount})
    return expenses  # Kembalikan daftar expenses


calculate_total_expenses = lambda expenses: sum(
    expense["jumlah"] for expense in expenses
)


def add_expense_interactively():
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    add_expense(date, description, amount)  # Gunakan fungsi add_expense
    print("Pengeluaran berhasil ditambahkan.")


def get_expenses_by_date(expense_list, target_date):
    filtered_expenses = [
        expense for expense in expense_list if expense["tanggal"] == target_date
    ]
    return filtered_expenses


def view_expenses_by_date():
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")


def main():
    view_expenses_by_date(expenses)


if __name__ == "__main__":
    main()
