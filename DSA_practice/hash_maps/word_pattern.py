'''290. Word Pattern
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false'''

#each letter in pattern has to match with only one word in sentence. 
#len of pattern and word count in s will be same. 

pattern = "abba" 
s = "dog cat cat fish"
ss = set(s.split(' '))
# general length checks, doesnt account for duplicates occuring consecutively
if len(set(pattern))!= len(set(s.split(' '))):
    print(False)
else:
    print(True)

# using zip_longest function to check for bijection property of two sets
from itertools import zip_longest
if (len(set(pattern)) == 
    len(set(s.split(' '))) ==
    len(zip_longest(pattern, ss))):
    print(True)
else:
    print(False)


