import numpy as np

# 1.1.1 从已有数据中创建数组
# 将列表专函为ndarray:
lst1 = [3, 2, 0, 1, 2]
nd1 = np.array(lst1)
print(nd1)
print(type(nd1))
print("*" * 30)

# 嵌套列表可以转换为多维ndarray
lst2 = [[3, 2, 0, 1, 2], [4, 5, 2, 1, 4]]
nd2 = np.array(lst2)
print(nd2)
print(type(nd2))
print("*" * 30)

# 1.1.2 利用random模块生成数组
nd3 = np.random.random([3, 3])
print(nd3)
print("nd3的形状为", nd3.shape)
print("*" * 30)
# 生成同一份数据，设置随机种子
np.random.seed(123)
nd4 = np.random.randn(2, 3)
print("未打乱数据")
print(nd4)
np.random.shuffle(nd4)
print("打乱之后的数据")
print(nd4)
print("*" * 30)

# 生成一个全为0的3*3矩阵
nd5 = np.zeros((3, 3))
print(nd5)
# 生成一个全为1的3*3矩阵，参照np5生成
nd6 = np.ones_like(nd5)
print(nd6)
# 生成3*3的单位矩阵
nd7 = np.eye(3)
print(nd7)
# 生成3阶对角矩阵
np8 = np.diag([1, 2, 3])
print(np8)
print("*" * 30)

# 将数组存起来，然后在去取
nd9 = np.random.random([5, 5])
np.savetxt(X=nd9, fname='./test1.txt')
pd10 = np.loadtxt('./test1.txt')
print(pd10)
print("*" * 30)

# arange函数的使用, arange(start, stop, step)
print(np.arange(10))
print(np.arange(1, 10))
print(np.arange(1, 4, 0.5))
print("*" * 30)

# linspace也是numpy模块中常用的函数，格式为np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
print(np.linspace(0, 1, 10))