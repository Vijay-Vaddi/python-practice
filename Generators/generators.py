# range doesnt store in memory but gives the items one by one where and when needed. 
# underneat the hood an iterable has __iter__ method
# range is an iterable and also a generator but list isnt an generator. 
# yeild pauses the function and comes back to it when next is called. yeild acts as generator and keeps track of next requests
# once range is over, the next next throws a StopIteration erros. The same is used in for loops while using range. 

# print(range(10))
# print(list(range(10)))

def generator_func(num):
    for i in range(num):
        yield i

nums = generator_func(2)
print(nums)
print(next(nums))
print(next(nums))