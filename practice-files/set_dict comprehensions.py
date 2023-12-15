# set comprehension same as list with {} instead of [] breaces

my_dict = {
    'a': 1,
    'b': 2 
}
# so create a dict with {key:val for key and val in dict.items()}
new_dict = {key:val for key, val in my_dict.items() if val%2==0}
# print(new_dict)


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dups =[]
dups = list(set([char for char in some_list if some_list.count(char) > 1]))
print(dups)