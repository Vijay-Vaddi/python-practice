#  Instead of generating all the values at once and returning them as a complete collection, a 
# generator generates one value at a time, and it "yields" that value to the caller, 
# maintaining its state between successive calls.

def fib(num):
    a = 0
    b = 1

    for i in range(num):
        yield a 
        temp = a
        a = b
        b = b + temp
    
for i in fib(10):
    print(i)
