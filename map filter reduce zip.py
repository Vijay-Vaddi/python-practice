#map takes an action (function) and an iterable and performs the action on the iterable
mylist = [1,2,3]
your_list = ['x','a','b','c']
def myltiply_2(item):
    return item*2

# print(list(map(myltiply_2, mylist)))

# Filters an iterable. All true values are returned 
def only_odd(item):
    return item % 2!=0

# print(list(filter(only_odd,mylist)))

# Zip takes multilple(more than one) iterables and zips them together

print(dict(zip(mylist,your_list, strict=False))) 

# Reduce reduces the iterable to a single value based on the function operated on the iterable.
# map and filter is using reduce under the hood it seems and reduce can be used to build our own map/filter like methods
from functools import reduce

def accumulator(initial_value, iter):
    return initial_value + iter

print(reduce(accumulator, mylist, 0))
