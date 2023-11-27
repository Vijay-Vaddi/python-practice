# when you wrap a fun inside another, and have a function returning another function
# python will know its a decorator function 
def my_decorator(func):
    def wrap_func():
        print('**')
        func()
    return wrap_func

#using @ and def a func will let python know you're kinda passing the hello() to decorator
@my_decorator
def hello():
    print('Hey there!!')

# when hello is called, hello() func is passed to decorator, fucn is wrapped and retured, and that fucn gets executed
@my_decorator
def bye():
    print("Bye bye Kenobi!!")

hello()
bye()

# # its the same as 
# a = my_decorator(hello)
# # my_decorator(hello)() is also same
# a()

