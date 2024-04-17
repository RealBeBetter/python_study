def absolute_value(x: int):
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x


print(absolute_value(2))

d = {'name': 'Real', 'birth': '2000-01-01', 'gender': 'male'}
for k in d:  # 遍历字典的键
    print(k)
# name
# birth
# gender

for v in d.values():  # 遍历字典的值
    print(v)
# Real
# 2000-01-01
# male

for k, v in d.items():  # 遍历字典的键值对
    print('key: {}, value: {}'.format(k, v))
# key: name, value: Real
# key: birth, value: 2000-01-01
# key: gender, value: male

for i in range(0, len(d), 1):
    print(i)
# 0
# 1
# 2

for i in range(len(d), 0, -1):
    print(i)
# 3
# 2
# 1

for i in range(1, -2, -1):
    print(i)

l = [1, 2, 3, 4, 5, 6, 7]
for index, item in enumerate(l):
    if index < 5:
        print(item)
# 1
# 2
# 3
# 4
# 5
