from functools import reduce


def multiply_by_two(input_list):
    # Membuat list baru dengan elemen-elemen hasil perkalian dua
    result_list = [x * 2 for x in input_list]
    return result_list


# Contoh penggunaan
my_list = [5, 4, 3, 2, 1]
result = multiply_by_two(my_list)
print(result)


hasil = []


def kali(list):
    for i in list:
        i = i * i
        hasil.append(i)
    return hasil


my_list = [5, 4, 3, 2, 1]

hasil = list(map(lambda x: x * x, my_list))
# hass = list(lambda x: x * x, my_list)
print(hasil)
# y = kali(my_list)
# print(y)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Contoh penggunaan
angka = 9
print(angka**0.5)
if is_prime(angka):
    print(f"{angka} adalah bilangan prima.")
else:
    print(f"{angka} bukan bilangan prima.")


# Menghitung nilai rata-rata dari daftar
def add(x, y):
    return x + y


numbers = [1, 2, 3, 4, 5]
average = reduce(add, numbers)

print(average)  # 3.0


def fun(x):
    for i in range(x):
        yield x - i


y = fun(5)
print(next(y))
print(next(y))
print(next(y))

data = [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16], [5, 10, 15, 20]]

data2 = [[i * j for j in range(1, 5)] for i in range(1, 6)]
print(data, data2)
