'''290. Input: pattern = "abba", s = "dog cat cat dog" , Output: true
Input: pattern = "abba", s = "dog cat cat fish", Output: false'''
#each letter in pattern has to match with only one word in sentence. 
#len of pattern and word count in s will be same. 

pattern = "abba" 
s = "dog cat cat fish"
words = s.split(' ')
# # general length checks, doesnt account for duplicates occuring consecutively
if (len(set(pattern))!= len(set(words)) or 
    len(words)!= len(pattern)):
    print(False)
else:
    print(True)

# # using zip_longest function to check for bijection property of two sets
from itertools import zip_longest
if (len(set(pattern)) == 
    len(set(s.split(' '))) ==
    len(set(zip_longest(pattern, words)))):
    print(True)
else:
    print(False)

# without zip_longest function
# save split words as keys and check againts index of pattern
    
def pattern_match(pattern, words):
    map = dict()
    for i in range(len(words)):
        if words[i] not in map:
            
            map[words[i]] = pattern[i]
            print(words[i], ' ', map[words[i]])
        elif map[words[i]] != pattern[i]:
            return False
        # to check if unique words are matching to duplicate pattern letter
        if len(map.keys())!=len(set(map.values())):
            return False
        print(map.items())
    return True

print(pattern_match(pattern, words))
