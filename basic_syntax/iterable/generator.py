# encoding: utf-8
import time

import memory_profiler


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"函数 {func.__name__} 执行时长：{execution_time} 秒")
        return result

    return wrapper


@measure_execution_time
@memory_profiler.profile
def add_with_generator(num: int) -> int:
    return sum(x for x in range(num))


@measure_execution_time
@memory_profiler.profile
def add_with_iterable(num: int) -> int:
    return sum([x for x in range(num)])


num_arg = 100000
print(add_with_generator(num_arg))
print(add_with_iterable(num_arg))
