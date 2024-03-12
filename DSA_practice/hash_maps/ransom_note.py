from collections import defaultdict

ransomNote = 'aa'
magazine = 'ab'
def canConstruct(ransomNote, magazine) -> bool:
    mag_dict = dict()
    ran_dict = dict()
    # map and count items in both strings
    for item in magazine:
        if item not in mag_dict:
            mag_dict[item] = 1
        else: 
            mag_dict[item]+=1

    for item in ransomNote:
        if item not in ran_dict:
            ran_dict[item] = 1
        else: 
            ran_dict[item]+=1
    # check it item in ransom note and its count
    for key, value in ran_dict.items():
        if key not in mag_dict:
            return False
        elif value > mag_dict[key]:
            return False
    return True

def canConstructUsingList(ransomNote, magazine) -> bool:
    ransomNote = list(ransomNote)
    magazine = list(magazine)
    #make a list of each strings, remove if exists, return false if not. 
    for char in ransomNote:
        if char in magazine:
            magazine.remove(char)
        else:
            return False 
    return True

print(canConstruct(ransomNote, magazine))
