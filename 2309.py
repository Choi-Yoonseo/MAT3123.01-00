class Solution:
    def greatestLetter(self, s: str) -> str:
        s=set(s)
        a=[]
        for i in s:
            if(i.isupper()):
                if(i.lower() in s):
                    a.append(i)
        if(len(a)==0):
            return ""
        return sorted(a)[-1]