# list set and dict comprehensions

# to quickly generate lists out of iterable items and perform actions on it as needed

my_list = []

my_list = [char for char in 'hello']
my_list1 = [num for num in range(0,100)]
my_list2 = [num for num in range(0, 100) if num%2==0]

# so I want a list of items in which [(item) for (each items in) (iterable) (where the conditon is this)]
print(my_list2)