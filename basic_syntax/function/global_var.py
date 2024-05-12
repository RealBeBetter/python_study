# encoding: utf-8

x = 1


def func():
    global x
    x += 1


func()
print(x)