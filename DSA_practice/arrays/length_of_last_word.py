'''58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
 
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.'''

s = "Hello World"
t = "   fly me   to   the moon  "

items = t.split()

print(items)

# for i in items[-1::-1]:
#     if i !="":
#         print(len(i))
#         break


        



