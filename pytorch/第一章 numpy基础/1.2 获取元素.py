import numpy as np

np.random.seed(2019)
nd1 = np.random.random([10])
print(nd1)
# 获取数据
nd2 = nd1[3]        # 获取第四个元素
print(nd2)
nd3 = nd1[3:6]      # 截取一部分元素
print(nd3)
nd4 = nd1[1:6:2]    # 截取固定间隔数据（第一个数字为开始取数的位置，第二个是结束的位置，第三个是步长（也就是取数间隔））
print(nd4)
print('*'*30)


nd5 = np.arange(25).reshape([5, 5])
print(nd5)
# 截取一个多维数组中，数值在一个值域之内的数据
nd6 = nd5[0:2, 1:3]     # 第一个0:2代表的是截取的对应的行数。从下标开始，第0行和第一行，后面的1:3是截取的列数，同样从下标开始
print(nd6)
nd7 = nd5[:, 1:3]       # 即不指定行，取列对应的所有值
print(nd7)
