import gc
import os

import psutil


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


show_memory_info('initial')

a = [i for i in range(10000000)]

show_memory_info('after a created')

del a
gc.collect()

show_memory_info('finish')
print(a)

# initial memory used: 6.734375 MB
# after a created memory used: 390.921875 MB
# Traceback (most recent call last):
#   File "C:\Users\Xxx\manual_collect.py", line 26, in <module>
#     print(a)
# NameError: name 'a' is not defined
# finish memory used: 7.60546875 MB
