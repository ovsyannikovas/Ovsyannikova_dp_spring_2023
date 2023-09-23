# Написать декоратор, который считает и выводит среднее время выполнения последних k вызовов исходной функции.
# k задается через параметр декоратора.
# После каждого вызова задекорированной функции должно выводиться среднее по k последним вызовам.

import time
import collections

def mean_deco(k=1):
    dq = collections.deque(maxlen=k)
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            val = func(*args, **kwargs)
            end_time = time.time() - start_time
            dq.append(end_time)
            print(sum(dq) / len(dq))
            return val
        return wrapper
    return decorator

@mean_deco(10)
def foo(arg1):
    time.sleep(0.1)
    return 10

# @mean_deco(2)
def boo(a, b):
    return a + b

for _ in range(100):
    foo("Walter") # при каждом вызове выводится среднее по k=10 последним вызовам