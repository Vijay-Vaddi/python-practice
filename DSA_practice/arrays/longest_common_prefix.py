
def longestCommonPrefix(strs) -> str:
    res = ''
    
    # for i in range(len(strs[0])):
    #     for j in range(1, len(strs)):
    #         if i>=len(strs[j]) or strs[j][i]!=strs[0][i]:
    #             return res 
    #     res+=strs[0][i]
    
    #sort alphabetically
    strs= sorted(strs)

    first = strs[0]
    last = strs[-1]

    for i in range(min(len(first), len(last))):
        if (first[i]!=last[i]):
            return res
        res+=first[i]
    return res     

print(longestCommonPrefix())