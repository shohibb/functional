from matplotlib import pyplot as plt

# Mengimpor fungsi normal dari pustaka numpy.random
# Digunakan untuk menghasilkan sampel data dari distribusi normal
from numpy.random import normal

# Mengimpor fungsi mean dan std dari pustaka numpy
# Digunakan untuk menghitung rata-rata dan standar deviasi data
from numpy import mean, std

# Mengimpor distribusi normal dari pustaka scipy.stats
# Digunakan untuk analisis statistik terkait distribusi normal
from scipy.stats import norm

sample = normal(loc=50, scale=5, size=1000)
plt.figure(figsize=(5, 4))


sample_mean = mean(sample)
sample_std = std(sample)

disk = norm(sample_mean, sample_std)
values = [value for value in range(30, 70)]

probability = [disk.pdf(value) for value in values]
print(probability)

# sample mean and std
plt.hist(sample, bins=10, density=True)
plt.bar(values, probability)
plt.show()
print("Mean: %.3f\nStandard deviation: %.3f" % (sample_mean, sample_std))
