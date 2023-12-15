new_dict = dict()
new_dict_list = [
    {
    'a':[1,2,3],
    'b':'Hello',
    3:123
    },
    {
    'a':[4,5,6],
    'b':'Hello',
    3:123
    },
    {
    'a':[1,2,3],
    'b':'Hello',
    'b': '123x' #over writes previous key:value
    } 
]
print(new_dict_list[1]['a'][2])
print(new_dict_list[2]['b'])
