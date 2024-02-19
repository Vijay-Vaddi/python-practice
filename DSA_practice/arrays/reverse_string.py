string = ['1','2']
print(type(string) is str)


#list comprehension
print(string[::-1])

print("".join(reversed(string)))

def rev(string):
    i=len(string)-1
    rev_str = []

    if len(string)>1 and type(string) is str or type(string) is list: 
        while i >=0:
            rev_str.append(string[i]) 
            i = i-1
        return "".join(rev_str)
    else: 
        return 'No good'
    

print(rev(string))
