# encoding: utf-8
from functools import reduce

square = lambda x: x ** 2
print(square(3))  # 9

range_list = [(lambda x: x * x)(x) for x in range(10)]
print(range_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1])  # 按列表中元祖的第二个元素排序
print(l)  # [(2, -1), (3, 0), (9, 10), (1, 20)]

squared = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(squared))

squared = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(squared)


def square(x):
    return x ** 2


squared = list(map(square, [1, 2, 3, 4, 5]))
print(squared)


def multiply(l):
    """
    side effect, multi call will return different result
    :param l:
    :return:
    """
    for index in range(0, len(l)):
        l[index] *= 2
    return l


def multiply_pure(l):
    """
    pure function, no side effect, multi call will return same result
    :param l:
    :return:
    """
    new_list = []
    for item in l:
        new_list.append(item * 2)
    return new_list


l = [1, 2, 3, 4, 5]
new_list = map(lambda x: x * 2, l)
print(list(new_list))  # [2, 4, 6, 8, 10]

new_list = filter(lambda x: x % 2 == 0, l)
print(list(new_list))  # [2, 4]

result = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(result)  # 1*2*3*4*5 = 120


d = {'mike': 10, 'lucy': 2, 'ben': 30}
dic = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(d)
print(dic)
