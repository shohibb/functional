import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10
interval_start = 150
interval_end = 200

# Menghitung batas-batas interval
interval_bins = np.arange(interval_start, interval_end, interval_size)

counts, bins, _ = plt.hist(tinggi_badan, bins=interval_bins, density=True, label="data")

# Mengelompokkan tinggi badan ke dalam interval
tinggi_badan_kelompok = np.digitize(tinggi_badan, interval_bins)

mean = np.mean(tinggi_badan)
std = np.std(tinggi_badan)
disk = norm(mean, std)


pdf = np.linspace(interval_start, interval_end, 100)
wee = norm.pdf(pdf, mean, std) * len(tinggi_badan) * interval_size
pdf = [disk.pdf(value) for value in bins]

# Menampilkan histogram
plt.plot(bins, pdf, label="PDF", color="red")
plt.title("Histogram Frekuensi tinggi badan")
plt.xlabel("Interval Tinggi Badan")
plt.ylabel("Frekuensi")
plt.legend()
plt.show()
