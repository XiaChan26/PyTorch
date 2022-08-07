import torch
# 设置一个随机种子
torch.manual_seed(100)
# 生成一个2*3的矩阵
x = torch.randn(2, 3)
print(x)
# 根据索引获取获取第一行，所有数据
x[0, :]
# 获取最后一列
x[:, -1]
# 生成是否大于0的Byter张量
mask = x > 0            # 输出的mask是True/False
print('mask', mask)
# 获取大于0的值
c = torch.masked_select(x, mask)
print('c', c)
# 获取非0下标，即行，列索引
d = torch.nonzero(mask)
print('d', d)
# 获取指定索引对应的值，输出根据以下规则得到
index = torch.LongTensor([[0, 1, 1]])
print('index', index)
e = torch.gather(x, 0, index)
print('e', e)
index = torch.LongTensor([[0, 1, 1], [1, 1, 1]])
a = torch.gather(x, 1, index)
# 把a的值返回到一个2*3的矩阵中
z = torch.zeros(2, 3)
print('z', z)
z.scatter_(1, index, a)
print(x)
print(z)

