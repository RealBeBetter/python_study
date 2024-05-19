def my_decorator(func):
    def wrapper(message):
        print('wrapper of decorator')
        func(message)

    return wrapper


@my_decorator
def greet(message):
    print(message)


greet('hello world')


# wrapper of decorator
# hello world


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


print(greet.__name__)  # wrapper
help(greet)

# Help on function my_decorator in module __main__:
#
# wrapper(message)
