class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum( [ (v-1)*v//2 for v in collections.Counter([ 10*min(i)+max(i) for i in dominoes ]).values() ]) 