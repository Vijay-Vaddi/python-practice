# def sayHi(name, age):
#     print("Hello there! " + name+ "you are " + str(age))
# # add a top to indent, no {} here in python
#
# sayHi("General Kenobi", 30)
# sayHi("General Grevios", 1)

# return statement

def cube(num):
    return num*num*num
    # print("check this out") noting executes after return
result = cube(4)
# print(result)

#if statements Need to put : after statement like functions to run
# indentation is needed
# is_male = False
# is_tall = True
# if is_male and is_tall:
#     print("you are a male and tall ")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("you are not male or tall")

##if statments and comparison
#comparison of values
'''
def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
# =, <=, !=, >=, ==
# print("largest is ", max_num(31,5,1))

# Translator

def translate(phrase):
    translation=""
    for ltr in phrase:
        if ltr.lower() in "aeiou": #converts ltr to lower and checks
        # if  ltr in "AEIOUaeiou": # will check if ltr is in any of these values. Cool!!
            if ltr.isupper():
                translation=translation+"G"
            else:
                translation=translation+"g"
        else:
            translation=translation+ltr
    return translation

print(translate(input("Enter a phrase")))
'''
''' 
Oh this is also a comment structure. its like /* */
kjdsfld
'''
# COMMENTS from video

# *args and **kwargs

def super_func(name, *args, hi='hey', **kwargs):
    print(*args)
    print(kwargs.values())

print(super_func('Vijay', 1,2,3,4,5, num1=5, num2=10))

#rule for sending values to functions
#params, *args, default parameters, **kwargs