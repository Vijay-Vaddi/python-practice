# .pyc (cache file) python c interpretor file is created in which all the imports of the main.py file are stored  
# from the second run of main.py, .pyc gets loaded directly... caching function!!!
# package is simply a folder containing modules

# import utility
# import shopping.cart

# print(utility.multiply(5,10))
# print(shopping.cart.add_to_cart('Apple'))

# more ways to import 
# from package inside of a package 

from shopping.more_shopping.cart import add_to_cart
# from utility import *
# from shopping.more_shopping import cart


# using __name__ 
# used to trace all the files the main.py runs through. the main is will always return __main__ irrespective of the name of the main file. 
print(__name__)

# used in python most of the time in project. 
# to controle the execution of the code only if its the main file, etc. 
if __name__ == "__main__":
    print("Hey its the main file only")
    print(add_to_cart('Banana'))

import random as rand

my_list = [1,2,3,4]
rand.shuffle(my_list)
print(my_list)