import re
# password validation with : a-zA-Z has 8 char min, $#%@ and ends with number
pattern = re.compile(r'[A-Za-z0-9$#%@]{8,}\d')

password = 'Hello@12345'
a = pattern.fullmatch(password)

print(a)
