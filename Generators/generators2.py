#generators are much faster.

from time import time

def performance(fn):
    def wrap_fun(*args, **kwargs):
        t1 = time()
        res = fn(*args, **kwargs)
        t2=time()
        print(t2-t1)
        return res
    return wrap_fun

@performance
def long_time1(num):
    for i in range(num):
        i*5

@performance
def long_time2(num):
    for i in list(range(num)):
        i*5

long_time1(10000000)
long_time2(10000000)


