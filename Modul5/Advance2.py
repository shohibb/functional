import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10  # Misalnya interval ukuran per 10 sentimeter

# Menambahkan interval tinggi badan dari 150-190
bins = np.arange(150, 191, interval_size)


# TODO 1: buat Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def interval_grouping(data, interval_size):
    return [(value // interval_size) * interval_size for value in data]


# TODO 2: Menghitung frekuensi tinggi badan dalam interval
frekuensi_interval = interval_grouping(tinggi_badan, interval_size)

# TODO 3: Visualisasi data dalam bentuk histogram
plt.hist(tinggi_badan, bins=bins, label="Data")

# TODO 4: Menambahkan kurva pdf pada hasil visualisasi data
mean, std_dev = np.mean(tinggi_badan), np.std(tinggi_badan)
x = np.linspace(min(tinggi_badan), max(tinggi_badan))
y = norm.pdf(x, mean, std_dev) * len(tinggi_badan) * interval_size
plt.plot(x, y, label="PDF Distribusi Normal", color="red")

plt.xlabel("Interval Tinggi Badan")
plt.ylabel("Frekuensi")
plt.title("Histogram Frekuensi Tinggi Badan")
plt.legend()
plt.show()
