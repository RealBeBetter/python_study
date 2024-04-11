d1 = {'name': 'Real', 'age': 24, 'gender': 'male'}
d2 = dict({'name': 'Real', 'age': 24, 'gender': 'male'})
d3 = dict([('name', 'Real'), ('age', 24), ('gender', 'male')])
d4 = dict(name='Real', age=24, gender='male')
print(d1 == d2 == d3 == d4)  # True

s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1 == s2)  # True

d = {'name': 'Real', 'age': 24}
print(d.get('name'))  # Real
print(d.get('location', 'null'))  # null
print(d["age"])  # 24
# print(d["location"])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'location'

s = {1, 2, 3}
# s[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'set' object is not subscriptable


s = {1, 2, 3}
print(1 in s)  # True
print(10 in s)  # False

d = {'name': 'Real', 'age': 24}
print('name' in d)  # True
print('location' in d)  # False

d = {'name': 'Real', 'age': 24, 'location': 'guangdong'}
d['gender'] = 'male'  # 增加元素对 'gender': 'male'
d['birth'] = '2000-02-01'  # 增加元素对 'birth': '1999-02-01'
print(d)  # {'name': 'Real', 'age': 24, 'location': 'guangdong', 'gender': 'male', 'birth': '2000-02-01'}
d['birth'] = '2000-01-01'  # 更新键 'birth' 对应的值
d.pop('birth')  # 删除键为 'birth' 的元素对
print(d)  # {'name': 'Real', 'age': 24, 'location': 'guangdong', 'gender': 'male'}

s = {1, 2, 3}
s.add(4)  # 增加元素 4 到集合
print(s)  # {1, 2, 3, 4}
s.remove(4)  # 从集合中删除元素 4
print(s)  # {1, 2, 3}
s.pop()
print(s)  # {2, 3}

d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])  # 根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])  # 根据字典值的升序排序
print(d_sorted_by_key)  # [('a', 2), ('b', 1), ('c', 10)]
print(d_sorted_by_value)  # [('b', 1), ('a', 2), ('c', 10)]

s = {3, 4, 2, 1}
print(sorted(s))  # 对集合的元素进行升序排序，返回 [1, 2, 3, 4]
print(s)  # 这里本身也会改变 {1, 2, 3, 4}

d = {'name': 'Real', 'birth': '2000-01-01', 'gender': 'male'}
for key, value in d.items():
    hash_value = hash(key)
    print(f"Key: {key}, Value: {value}, Hash Value: {hash_value}")

d = {'gender': 'male', ('education', 'college'): ['Stanford University']}  # 正确
print(d)
d = {'gender': 'male',
     ['education', 'college', 'university']: ['Stanford University']}  # 错误 TypeError: unhashable type: 'list'
print(d)
