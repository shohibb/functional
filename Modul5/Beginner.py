import matplotlib.pyplot as plt
from functools import reduce

# Data nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]
nomor_mahasiswa = list(range(1, len(nilai_mahasiswa) + 1))


def average(numbers):
    sum = reduce(lambda x, y: x + y, numbers)
    average = sum / len(numbers)
    return average


result = average(nilai_mahasiswa)

plt.figure(figsize=(5, 5))
plt.bar(nomor_mahasiswa, nilai_mahasiswa)
plt.axhline(y=result, color="r", linestyle="--", label=f"Rata-rata: {result:.2f}")
plt.xlabel("Mahasiswa")
plt.ylabel("Nilai Ujian")
plt.legend()
plt.show()
