def borg_statement(func):
    def wrapper(*args, **kwargs):
        print(args[0])
        func(*args, **kwargs)
        print(args[2])
    return wrapper

@borg_statement
def borg(*args, **kwargs):
    print(args[1])

a, b, c ='we are', 'borg', 'resistance is futile'
borg(a, b, c)
