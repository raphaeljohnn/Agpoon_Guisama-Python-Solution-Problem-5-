import matplotlib.pyplot as plt
import numpy as np

n = np.arange(200).tolist()
item = np.array([])

for i in range(200):
    result = 3*np.pi*n[i]/100
    item = np.append(item, result)

a = np.sin(item)
b = -1.5*a[0] + 2*a[1] - 0.5*a[2]
for i in range(1, 199):
    result = 0.5*a[i+1] - 0.5*a[i-1]
    b = np.append(b, result)

b = np.append(b, 1.5*a[199] - 2*a[198] + 0.5*a[197])

plt.stem(n, b, 'y', markerfmt='yo', label='y(n)')
plt.stem(n, a, 'g', markerfmt='go', label='x(n)')
plt.legend()
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Graph of x(n) and y(n)')
plt.show()