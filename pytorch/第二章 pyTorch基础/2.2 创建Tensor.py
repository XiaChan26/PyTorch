import torch
# 根据list数据生成Tensor
x = torch.Tensor([1, 2])
print(x)
# 根据指定形状生成Tensor
u = torch.Tensor(2, 3)
print(u)
y = torch.tensor([3, 4])
z = x.add(y)
print(z)
x.add_(y)
o = torch.logspace(1, 2, 2)
print(o)
v = torch.Tensor(1)
print(v)