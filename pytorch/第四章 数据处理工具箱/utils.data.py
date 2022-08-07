# 1、导入需要的模块
import torch
from torch.utils import data
import numpy as np


# 2、定义获取数据集的类
# 该类继承基类Dataset，自定义一个数据集及对应标签，自定义Dataset需要重写__getitem__和__len__
class TestDataset(data.Dataset):
    def __init__(self):
        self.Data = np.asarray([[1, 2], [3, 4], [2, 1], [4, 2], [4, 5]])
        self.Label = np.asarray([0, 1, 0, 1, 2])

    def __getitem__(self, index):
        # 把numpy转化为Tensor
        txt = torch.from_numpy(self.Data[index])
        label = torch.tensor(self.Label[index])
        return txt, label

    def __len__(self):
        return len(self.Data)


# 3、获取数据集中数据
Test = TestDataset()
print(Test[2])
print(Test.__len__())

test_loader = data.DataLoader(Test, batch_size=2, shuffle=False)
for i, traindata in enumerate(test_loader):
    print('i:', i)
    Data, Label = traindata
    print('data:', Data)
    print('Label:', Label)
