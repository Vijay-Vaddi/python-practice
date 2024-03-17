# 28. Find the Index of the First Occurrence in a String

def strStr(haystack: str, needle: str) -> int:
    
    # if needle in haystack:
    #     return haystack.index(needle)
    # else:
    #     return -1 

    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    
    return -1

haystack = "sadbutsad" 
needle = "sad"
print(strStr(haystack, needle))