class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = [0]*(len(s)+1)
        i,j = 0,len(s)
        for k in range(len(s)):
            if s[k] == "I":
                res[k] = i
                i+=1
            else:
                res[k] = j
                j-=1
        if s[-1] == "I":
            res[-1] = i
        else:
            res[-1] = j
        return res  
