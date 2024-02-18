# given 2 arrays, create a function that lets a user know T/F, if 
# arrays have common items
array1 = ['a','b','i','c']
array2 = ['z','y','c']

# brute force 
# O(n*m) or O(n^2)
def brute_force_common_items(array1, array2):
    for a in array1:
        for b in array2:
            if a == b: 
                return True
    return False

# hash set
# it wont matter weather duplicates are there or not in this case
# since only common items matter.
# O(n+m+1) --> O(m+n) linear, better 
def hash_set_common_items(array1, array2):
    set1 = set(array1) #O(n)
    for item in array2: #O(m)
        if item in set1: #O(1)
            return True 
    return False

#to save even more but negligible time
 
def len_hash_set_common_items(array1, array2):
    if len(array2) > len(array1):
        set_items = set(array2) #O(n)
        for item in array1: #O(n)
            if item in set_items: #O(1)
                return True 
    elif len(array2) < len(array1):
        set_items = set(array1) #O(n)
        for item in array2: #O(n)
            if item in set_items: #O(1)
                return True           
    return False

# langage specific
set_items = set(array2)
if any(item in set_items for item in array1):
    print(True)

# print(hash_set_common_items(array1=array1, array2=array2))
# print(brute_force_common_items(array1=array1, array2=array2))
