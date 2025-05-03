import numpy as np
import matplotlib.pyplot as plt

# 1. Гистограмма для случайных данных с нормальным распределением
mean = 0
std_dev = 1
num_samples = 1000
data_normal = np.random.normal(mean, std_dev, num_samples)

plt.figure(figsize=(8, 6))
plt.hist(data_normal, bins=30, density=True, alpha=0.7, color='skyblue')
plt.title('Гистограмма случайных данных (нормальное распределение)')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 2. Диаграмма рассеяния для двух наборов случайных данных
num_points = 50
data_rand_x = np.random.rand(num_points)
data_rand_y = np.random.rand(num_points)

plt.figure(figsize=(8, 6))
plt.scatter(data_rand_x, data_rand_y, alpha=0.6, color='salmon')
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('Значение X')
plt.ylabel('Значение Y')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()