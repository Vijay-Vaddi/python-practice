# 151. Reverse Words in a String

def reverseWords(s: str) -> str:
    
    s = s.split(' ')
    res = [word for word in s[::-1] if word!='']
    return ' '.join(res)

s = "the sky is blue"

print(reverseWords(s))