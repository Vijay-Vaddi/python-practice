# regEx comes as a module in python
import re

string = 'search inside of this text please'
# print('search' in string) works. but limited
# returns none if no match
a = re.search('this', string) #gives index of begining and end of search
# print(a.span())
# span gives indexes, start(), end() gives index, group gives part of the string that was a match
# print(a.group())    

pattern = re.compile('search inside of this text please!')

b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string) #matches first characters until no match
print(d)
