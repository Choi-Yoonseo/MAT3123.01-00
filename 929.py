class Solution:
    def numUniqueEmails(self, A):
        D = set()
        for x in A:
            a,b = x.split('@')
            a   = a.split('+')[0]
            a   = a.replace('.','')
            D.add( (a,b) )
        return len(D)