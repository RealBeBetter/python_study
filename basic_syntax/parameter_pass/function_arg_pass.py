def my_func1(b):
    b = 2


a = 1
my_func1(a)
print(a)  # 1


def my_func2(b):
    b = 2
    return b


a = 1
a = my_func2(a)
print(a)  # 2


def my_func3(l2):
    l2.append(4)


l1 = [1, 2, 3]
my_func3(l1)
print(l1)  # [1, 2, 3, 4]


def my_func4(l2):
    l2 = l2 + [4]


l1 = [1, 2, 3]
my_func4(l1)
print(l1)  # [1, 2, 3]


def my_func5(l2):
    l2 = l2 + [4]
    return l2


l1 = [1, 2, 3]
l1 = my_func5(l1)
print(l1)  # [1, 2, 3, 4]
