import time
from multiprocessing import Process


def task():
    # 执行任务
    count_down(100000000 / 5)


def count_down(n):
    while n > 0:
        n -= 1


processes = []
for _ in range(5):
    p = Process(target=task)
    p.start()
    processes.append(p)

start_time = time.perf_counter()
for p in processes:
    p.join()
end_time = time.perf_counter()
print('总共耗时：{:.2f}s'.format(end_time - start_time))
# 总共耗时：0.22s
