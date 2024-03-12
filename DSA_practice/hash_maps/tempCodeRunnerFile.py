 checks, doesnt account for duplicates occuring consecutively
# if (len(set(pattern))!= len(set(words)) or 
#     len(words)!= len(pattern)):
#     print(False)
# else:
#     print(True)

# # using zip_longest function to check for bijection property of two sets
# from itertools import zip_longest
# if (len(set(pattern)) == 
#     len(set(s.split(' '))) ==
#     len(set(zip_longest(pattern, words)))):
#     print(True)
# else:
#     print(False)