# methods of debugging

# linting : the red underline in IDE. VScode has PI lint extension for use. 

# num + 4

# pdb : python debugger 

import pdb
# can change input while doing pdb. 

def add(num1, num2):
    pdb.set_trace()
    # traces the code dude. 
    # learn this properly
    return num1+num2

print(add(1, 'hel'))
