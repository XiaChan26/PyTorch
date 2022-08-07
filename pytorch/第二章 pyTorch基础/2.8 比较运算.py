import torch
x = torch.linspace(0, 10, 6).view(2, 3)
print(x)
# 求所有元素最大值
b = torch.max(x)
print(b)
# 求y轴最大值
c = torch.max(x, dim=0)
print('c', c)
# 求最大的两个元素
d = torch.topk(x, 1, dim=0)
print('d', d)