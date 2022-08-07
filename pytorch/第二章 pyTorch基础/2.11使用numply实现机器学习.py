import numpy as np
from matplotlib import pyplot as plt
np.random.seed(100)
x = np.linspace(-1, 1, 100).reshape(100, 1)
print(x)
y = 3*np.power(x, 2) + 0.2*np.random.rand(x.size).reshape(100, 1)
print(y)
plt.scatter(x, y)
plt.show()