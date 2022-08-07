import torch
t = torch.randn(1, 3)
t1 = torch.randn(3, 1)
t2 = torch.randn(1, 3)
# t+0.1*(t1/t2)
a = torch.addcdiv(t, 0.1, t1, t2)
print(a)
# 计算sigmoid
b = torch.sigmoid(t)
print(b)
# 将t限制在[0，1]之间
c = torch.clamp(t, 0, 1)
print(c)
# t+2进行就地计算
d = t.add_(2)
print(d)
