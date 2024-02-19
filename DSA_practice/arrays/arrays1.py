strings = ['a', 'b', 'c', 'd']
# 4*4 = 16 bytes of storage on 32 bit system

# add/push 
strings.append('e') #O(1) O(n) if memory relocation needed. 

# pop/remove at the end of array  
strings.pop() # o(1)

# shift/unshift appending at the beginning
# x = ['x']
# x.extend(strings) 
# O(n)

strings.insert(0, 'x') #O n 
#faster than strings = ['x']+strings

strings[:0] = ['y'] #O n

# from double ended queue
from collections import deque
de_string = deque(strings)
de_string.appendleft('q')
# o (1) time
# o (1) auxiliary space

print(strings) 
print(list(de_string))


