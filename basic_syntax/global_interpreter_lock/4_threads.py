import time
from threading import Thread


def count_down(n):
    while n > 0:
        n -= 1


n = 100000000

start_time = time.perf_counter()
t1 = Thread(target=count_down, args=[n // 4])
t2 = Thread(target=count_down, args=[n // 4])
t3 = Thread(target=count_down, args=[n // 4])
t4 = Thread(target=count_down, args=[n // 4])

t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
end_time = time.perf_counter()
# finished in 2.9052210999652743 seconds
print(f'finished in {end_time - start_time} seconds')
