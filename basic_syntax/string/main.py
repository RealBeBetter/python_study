name = 'Real'
city = 'shenzhen'
text = "Hello World"

s1 = 'hello'
s2 = "hello"
s3 = """hello"""
print(s1 == s2 == s3)  # True


def calculate_similarity(item1, item2):
    """
    Calculate similarity between two items
    Args:
        item1: 1st item
        item2: 2nd item
    Returns:
      similarity score between item1 and item2
    """


s = 'a\nb\tc'
print(s)
# a
# b	c

name = "Real"
print(name[0])  # R
print(name[1:3])  # ea

for char in name:
    print(char)
# R
# e
# a
# l

s = 'hello'
# s[0] = 'H'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     s[0] = 'H'
# TypeError: 'str' object does not support item assignment

new_str = 'H' + s[1:]  # 用大写的'H'，通过加号'+'操作符，与原字符串切片操作的子字符串拼接而成新的字符串
new_str = s.replace('h', 'H')  # 扫描原字符串，把小写的'h'替换成大写的'H'，得到新的字符串。

s = ''
for n in range(0, 100000):
    s += str(n)

# 使用 string.join(iterable) 函数拼接每个元素
l = []
for n in range(0, 100000):
    l.append(str(n))
l = ' '.join(l)


# 使用 string.split(separator) 将字符串按照 separator 分割成子字符串
# 返回一个分割后子字符串组合的列表
def query_data(namespace, table) -> []:
    """
    given namespace and table, query database to get corresponding
    data
    """


path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0]  # 返回'ads'
table = path.split('//')[1].split('/')[1]  # 返回 'training_table'
data = query_data(namespace, table)
print(data)

# string.strip(str)，表示去掉首尾的 str 字符串
# string.lstrip(str)，表示只去掉开头的 str 字符串
# string.rstrip(str)，表示只去掉尾部的 str 字符串


user_id = 1000
name = "Real"

print('no data available for person with id: {}, name: {}'.format(user_id, name))
# no data available for person with id: 1000, name: Real

print("no data available for person with id: %d, name: %s" % (user_id, name))
# no data available for person with id: 1000, name: Real

print(f"no data available for person with id: {user_id}, name: {name}")
# no data available for person with id: 1000, name: Real

print(f"no data available for person with id: {user_id}, name: {name}")
