from contextlib import contextmanager


@contextmanager
def file_manager(name, mode):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()


with file_manager('test.txt', 'w') as f:
    f.write('hello world')
