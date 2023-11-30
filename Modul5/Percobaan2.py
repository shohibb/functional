import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([3, 3, 6, 6])
ypoints = np.array([3, 10, 3, 10])

xpoints2 = np.array([4, 4, 7, 7])
ypoints2 = np.array([3, 10, 3, 10])

plt.figure(figsize=(5, 5))
plt.plot(xpoints, ypoints, color="red", label="data x,y", marker="x")
plt.plot(xpoints2, ypoints2, color="black", label="data x,y", marker="o")

plt.xlabel("sumbu x")
plt.ylabel("sumbu y")
plt.title("grafik x dan y")
plt.xlim([0, 15])
plt.ylim([0, 15])
plt.legend()
plt.show()
