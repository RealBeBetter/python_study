# encoding: utf-8
import timeit
from collections import namedtuple
from pprint import pprint

ls = [1, 2, 'hello', 'world']  # 列表中同时含有 int 和 string 类型的元素

tup = (1, 2, 3, 4)
new_tup = tup + (5,)  # 创建新的元组 new_tup，并依次填充原元组的值
# 新元组的值为 (1, 2, 3, 4, 5)

print(ls)

print(tup)
print(new_tup)

l = [1, 2, 3, 4]
print(l[-1])  # 4

tup = (1, 2, 3, 4)
print(tup[-1])  # 4

l = [1, 2, 3, 4]
print(l[1:3])  # 返回列表中索引从 1 到 2 的子列表, [2, 3]

tup = (1, 2, 3, 4)
print(tup[1:3])  # 返回元组中索引从 1 到 2 的子元组, (2, 3)

point = namedtuple('Point', ['x', 'y'])

l = [[1, 2, 3], [4, 5]]  # 列表的每一个元素也是一个列表
print(l)

tup = ((1, 2, 3), (4, 5, 6))  # 元组的每一个元素也是一元组
print(tup)

print(list((1, 2, 3)))  # [1, 2, 3]

print(tuple([1, 2, 3]))  # (1, 2, 3)

# 常用函数
l = [3, 2, 3, 7, 8, 1]
l.count(3)  # 结果为 2，统计元素出现的个数，表示 3 出现了 2 次
l.index(7)  # 结果为 3，返回元素在列表中的索引
l.reverse()  # 无返回值，将 list 反转
l.sort()  # 无返回值，将 list 排序
print(l)  # 顺序改变

tup = (3, 2, 3, 7, 8, 1)
tup.count(3)  # 2，统计元素出现的个数，表示 3 出现了 2 次
tup.index(7)  # 3，返回元素在元组中的索引
list(reversed(tup))  # 将元组反转，需要使用 list 函数转换
sorted(tup)  # 将元组排序，返回一个新的元组
print(tup)  # 顺序不变

# 存储方式
l = [1, 2, 3]
print(l.__sizeof__())  # 72
tup = (1, 2, 3)
print(tup.__sizeof__())  # 48

l = []
l.__sizeof__()  # 空列表的存储空间为 40 字节
# 40
l.append(1)
l.__sizeof__()  # 72 加入了元素 1 之后，列表为其分配了可以存储 4 个元素的空间 (72 - 40)/8 = 4
l.append(2)
l.__sizeof__()  # 72 由于之前分配了空间，所以加入元素 2，列表空间不变
l.append(3)
l.__sizeof__()  # 72 同上
l.append(4)
l.__sizeof__()  # 72 同上
l.append(5)
l.__sizeof__()  # 104 加入元素 5 之后，列表的空间不足，所以又额外分配了可以存储 4 个元素的空间

timeit.Timer('x=(1,2,3,4,5,6)').timeit(number=1000000)  # 0.010569700039923191
timeit.Timer('x=[1,2,3,4,5,6]').timeit(number=1000000)  # 0.041034199995920060


def index_tuple():
    x = (1, 2, 3, 4, 5, 6)
    return x[3]


def index_list():
    x = [1, 2, 3, 4, 5, 6]
    return x[3]


print(timeit.Timer(lambda: index_tuple()).timeit(number=1000000))  # 0.09114550007507205
print(timeit.Timer(lambda: index_list()).timeit(number=1000000))  # 0.12712049996480346

x = (1, 2, 3, 4, [1, 2])
print(x)  # (1, 2, 3, 4, [1, 2])

x[4].append(3)
print(x)  # (1, 2, 3, 4, [1, 2, 3])
