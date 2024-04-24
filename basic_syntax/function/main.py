# encoding: utf-8

def function_name(param: int = 1) -> int:
    # do something
    # yield/return param
    return param


# print_func('hello world')
#
#
# def print_func(message):
#     print('Got a message: {}'.format(message))

# 输出
# NameError: name 'print_func' is not defined


def my_func(message):
    my_sub_func(message)  # 调用 my_sub_func() 在其声明之前不影响程序执行


def my_sub_func(message):
    print('Got a message: {}'.format(message))


# my_func('hello world')


# 输出
# Got a message: hello world


def f1():
    print('hello')

    def f2():
        print('world')

    f2()


f1()


# 输出
# hello
# world


def factorial(input_val):
    # validation check
    if not isinstance(input_val, int):
        raise Exception('input must be an integer.')
    if input_val < 0:
        raise Exception('input must be greater or equal to 0')

    def inner_factorial(value):
        if value <= 1:
            return 1
        return value * inner_factorial(value - 1)

    return inner_factorial(input_val)


print(factorial(5))

MIN_VALUE = 1
MAX_VALUE = 10


def validation_check():
    global MIN_VALUE
    MIN_VALUE += 1


validation_check()
print(MIN_VALUE)  # 2


def outer():
    x = "local"

    def inner():
        nonlocal x  # nonlocal 关键字表示这里的 x 就是外部函数 outer 定义的变量 x
        x = 'nonlocal'
        print("inner:", x)

    inner()
    print("outer:", x)


outer()


# 输出
# inner: nonlocal
# outer: nonlocal


def outer():
    x = "local"

    def inner():
        x = 'nonlocal'  # 这里的 x 是 inner 这个函数的局部变量
        print("inner:", x)

    inner()
    print("outer:", x)


outer()


# 输出
# inner: nonlocal
# outer: local


def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是 exponent_of 函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方
print(square)  # <function nth_power.<locals>.exponent_of at 0x00000227077CC820>
print(cube)  # <function nth_power.<locals>.exponent_of at 0x00000227077CC8B0>

print(square(2))  # 4
print(cube(2))  # 8
