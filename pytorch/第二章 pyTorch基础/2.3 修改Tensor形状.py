import torch
# 生成一个形状为2*3的矩阵
x = torch.randn(2, 3)
print(x)
# 查看矩阵形状
print(x.size())
# 查看维度
print(x.dim())
# 把x变成3*2的矩阵
y = x.view(3, 2)
print(y.size())
# 将x展平
z = x.view(-1)
print(z)
# 添加一个维度
p = torch.unsqueeze(z, 0)
print('p', p)
# 查看元素个数
u = p.numel()
print(u)