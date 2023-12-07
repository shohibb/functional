import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

produk, harga, jumlah_terjual = zip(*data_transaksi)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

colors = np.random.uniform(15, 80, len(data_transaksi))
axs[0].scatter(harga, jumlah_terjual, c=colors)
axs[0].set_xlabel("Harga Produk")
axs[0].set_ylabel("Jumlah Produk Terjual")

total_pendapatan = [harga[i] * jumlah_terjual[i] for i in range(len(data_transaksi))]

axs[1].bar(produk, total_pendapatan, color="blue", alpha=0.7)
axs[1].set_title("Total Pendapatan untuk Setiap Produk")
axs[1].set_xlabel("Total Pendapatan")
axs[1].set_ylabel("Produk")

# Tampilkan plot
plt.tight_layout()
plt.show()
