# encoding: utf-8

x = [1]


def func():
    x.append(2)


func()
print(x)  # [1, 2]
