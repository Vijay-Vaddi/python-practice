from collections import Counter, defaultdict, OrderedDict
from array import array

dict = defaultdict(lambda: 'does not exist', {'a':1})
# # dict = {'a':1}

print(dict['b'])

arr = array('i', [1,2,4,5])
print(arr[0])


