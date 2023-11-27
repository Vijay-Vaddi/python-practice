# how for loops works underneat the hood
# object the same memory. 

def create_for_loop(iterable):
    iterator = iter(iterable)
    # the iter function allows us to use the next function
    while True:
        try:
            print(iterator) #print object location in memory
            print(next(iterator))
        except StopIteration:
            break

create_for_loop([1,2,3,4])