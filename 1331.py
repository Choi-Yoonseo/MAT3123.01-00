class Solution:
   def arrayRankTransform(self, arr: List[int]) -> List[int]:
       b,o,c = {},1,arr.copy()
       c.sort()
       re=[]
       for i in c:
           if i not in b:
               b[i] = o
               o+=1
       for i in range(len(arr)):
           re.append(b[arr[i]])
       return re
   	