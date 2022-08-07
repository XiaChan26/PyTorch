import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 1], [1, 2]])
C = A * B
print(A)
# 或者
D = np.multiply(A, B)
print(C)
print(D)

# 还满足和单一数值进行运算
E = A * 2
print(E)
print('*' * 30)

# 实现激活函数实验
X = np.random.rand(2, 3)
print(X)


def softmoid(x):
    return 1 / (1 + np.exp(-x))


print(softmoid(X))
print('*' * 30)
# 点积
X1 = np.array([[1, 2], [1, 3]])
X2 = np.array([[2, 3, 3], [2, 3, 4]])
X3 = np.dot(X1, X2)
print(X3)