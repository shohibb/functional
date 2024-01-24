# 1. Data tuple:
tup = ("Pensil", 1500, "Buku", 5000, "Penggaris", 2000)
# 2. Fungsi untuk memisahkan data tuple:
liststr = []
listint = []


def split(tuple):
    for i in tuple:
        if isinstance(tuple, str):
            liststr.append(i)
        elif isinstance(tuple, int):
            listint.append(i)


split(tup)
print(liststr)
# 3. Fungsi untuk membuat dictionary:

# 4. Hasil:
