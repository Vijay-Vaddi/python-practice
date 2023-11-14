# To pass arguments to decorated functions

def my_decorator(func):
    def wrap_func(*args,**kwargs):
        func(*args, **kwargs)
    return wrap_func

@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)

hello('Hello there', emoji='General Kenobi')