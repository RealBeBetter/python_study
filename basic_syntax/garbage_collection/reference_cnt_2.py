import sys

a = []

print(sys.getrefcount(a))  # 两次

b = a

print(sys.getrefcount(a))  # 三次

c = b
d = b
e = c
f = e
g = d

print(sys.getrefcount(a))  # 八次
