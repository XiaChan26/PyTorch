import numpy as np

# 1 . reshape , 改变向量的维度，不修改向量本身
arr = np.arange(10)
print(arr)
# 将维度变为（2, 5）
arr1 = arr.reshape(2, 5)
print(arr1)
# 指定时，可以只指定行或者列，另外一个用-1代替
arr2 = arr.reshape(-1, 2)
print(arr2)
print('*' * 30)
arr.resize(2, 5)
print(arr)
print('*' * 30)

# 展平
X = np.arange(6).reshape(2, -1)
print(X)
X1 = X.ravel()
print(X1)
X2 = X.ravel('F')
print(X2)
print('*' * 30)
# 矩阵转化为向量
a = np.floor(10 * np.random.random((3, 4)))
print(a)
print(a.flatten())
print('*' * 30)
# 降维
Q = np.arange(3).reshape(3, 1)
print(Q)
print(Q.squeeze())
print(Q.squeeze().shape)
print('*' * 30)

# ========================合并数组==========================================
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
c = np.append(a, b)
print(c)

# 多维
d = np.arange(4).reshape(2, 2)
e = np.arange(4).reshape(2, 2)
# append按照行合并
f = np.append(d, e, axis=0)
print(f)
# append按照列合并
g = np.append(d, e, axis=1)
print(g)
print('*=' * 30)

# concatenate
i = np.array([[1, 2], [3, 4]])
k = np.array([[1, 2]])
print(i)
# 按照行
j = np.concatenate((i, k), axis=0)
print(j)
# 按照列
l = np.concatenate((i, k.T), axis=1)
print(l)

# stack
m = np.array([[1, 2], [3, 4]])
n = np.array([[1, 2], [3, 4]])
print(np.stack((m, n), axis=0))