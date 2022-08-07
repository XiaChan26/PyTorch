import numpy as np
# 生成10000个形状维2*3的矩阵
data_train = np.random.randn(10000, 2, 3)
# 这是一个3维矩阵，第一个维度为样本数，后面两个为数据形状
print(data_train.shape)
# 打乱数据
np.random.shuffle(data_train)
# 定义批大小
batch_size = 100
# 进行批处理
for i in range(0, len(data_train), batch_size):
    x_batch_sum = np.sum(data_train[i:i+batch_size])
    print("第{}批次，该批次的数据之和：{}".format(i, x_batch_sum))