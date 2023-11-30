import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]
sizes = np.random.uniform(5, 90, len(x))
colors = np.random.uniform(15, 80, len(x))
plt.scatter(x, y, s=sizes, c=colors)
plt.show()
