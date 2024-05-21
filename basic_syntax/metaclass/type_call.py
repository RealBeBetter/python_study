class MyClass:
    data = 1


instance = MyClass()
print(MyClass, instance)
# <class '__main__.MyClass'> <__main__.MyClass object at 0x000001F21FDABFD0>
print(instance.data)
# 1

MyClass = type('MyClass', (), {'data': 1})
instance = MyClass()
print(MyClass, instance)
# <class '__main__.MyClass'> <__main__.MyClass object at 0x000001F21FDABF40>
print(instance.data)
# 1
