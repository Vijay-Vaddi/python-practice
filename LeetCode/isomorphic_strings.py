from collections import defaultdict

s = "egg" 
t = "add"

def isIsomorphic(s: str, t: str) -> bool:
        
    # put letter from one string as key and the other as value, 
    # if the key exists and the value isnt the same, then false

    if len(s)!= len(t):
        return False 
    map1 = defaultdict()
    map2 = defaultdict()

    for i in range(len(s)):
        if s[i] in map1:
            if map1[s[i]]!= t[i]:
                return False
        map1[s[i]] = t[i]

        if t[i] in map2:
            if map2[t[i]]!= s[i]:
                return False
            
        map2[t[i]] = s[i]

    print(map1.keys())
    print(map2.values())
        
    if list(map1.keys()) == list(map2.values()):
        print('here')
        return True
    else:
        return False
    return True 

print(isIsomorphic(s, t))