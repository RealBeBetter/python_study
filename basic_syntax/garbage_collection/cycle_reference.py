import gc
import os

import psutil


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after a, b created')
    a.append(b)
    b.append(a)


func()
gc.collect()
show_memory_info('finished')

# initial memory used: 6.80078125 MB
# after a, b created memory used: 774.70703125 MB
# finished memory used: 8.0546875 MB

# 未调用 gc.collect() 的情况
# initial memory used: 6.59375 MB
# after a, b created memory used: 773.953125 MB
# finished memory used: 773.953125 MB
