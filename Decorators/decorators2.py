# To pass arguments to decorated functions

def my_decorator(func):
    def wrap_func(*args,**kwargs):
        func(*args, **kwargs)
    return wrap_func

@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)

hello('Hello there', emoji='General Kenobi')

# how and why it can be useful

from time import time

def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args,**kwargs)
        t2 = time()
        print(f'It took {t2-t1} seconds to run this code')
        return result
    return wrap_func
    
# this way, decorators can be used to test perfomance, log activities, add features to main (passed) function
@performance
def long_multiply():
    for i in range(100000000):
        i*5

long_multiply()
