class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        Count1=0
        Range=[]
        Binary=[]
        Values=[]
        for i in range(left, right+1):
            Range.append(i)
        for i in Range:
            Binary.append(bin(i)[2:])
        for i in Binary:
            Count=0
            for j in i:
                if j=="1":
                    Count+=1
            Values.append(Count)
        for i in Values:
            if i>1:
                Flag=True
                for j in range(2,int(i**0.5)+1):
                    if i%j==0:
                        Flag=False
                if Flag:
                    Count1+=1
        return Count1