import torch
a = torch.tensor([2, 3])
b = torch.tensor([3, 4])
c = torch.dot(a, b)
print(c)
x = torch.randint(10, (2, 3))
print(x)
y = torch.randint(6, (3, 4))
print(y)
u = torch.mm(x, y)
print('u', u)
v = torch.randint(10, (2, 2, 3))
i = torch.randint(6, (2, 3, 4))
h = torch.bmm(v, i)
print(h)
