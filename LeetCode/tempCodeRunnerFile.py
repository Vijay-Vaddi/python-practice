        if t[i] in map2:
            if map2[t[i]]!= s[i]:
                return False
        map2[t[i]] = s[i]
