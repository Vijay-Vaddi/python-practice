def canConstruct(ransomNote, magazine) -> bool:
    
    mag_dict ={}
    for item in magazine:

        if item in mag_dict:
            mag_dict[item]+=1
        mag_dict[item] = 1
    
    for item in ransomNote:

        if item not in mag_dict and mag_dict[item]==0:
            return False
        else: 
            mag_dict[item]-=1
    
    return True

print(canConstruct(ransomNote = "a", magazine = "b"))
