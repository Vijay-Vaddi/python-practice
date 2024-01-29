# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

s = "anagram" 
t = "nagaram"

dic_s = {}
dic_t = {}

def check_anagrams(dic_s, dic_t):
    for char in sorted(s): 
        if char not in dic_s.keys():
            dic_s[char] = 1
        else:
            dic_s[char]+=1

    for char in sorted(t): 
        if char not in dic_t.keys():
            dic_t[char] = 1
        else:
            dic_t[char]+=1

    print(dic_t.items(), '\n', dic_s.items())
    return dic_s.items() == dic_t.items() #dic_t.keys() == dic_s.keys() and dic_s.values() == dic_t.values()

print(check_anagrams(dic_s, dic_t)) 