# one time anonymous functions which isnt likely used more than once. 
# saves memmory, clean code 
#  lambda parameter : operation_on_parameter 
from functools import reduce
items = [1,2,3]

print(list(filter(lambda item : item%2!=0, items)))

print(reduce(lambda acc, item : acc+item, items))

print(list(map(lambda item : item**2, items)))

a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key = lambda a: a[1])
print(a)
