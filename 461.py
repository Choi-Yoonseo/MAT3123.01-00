class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        dist = 0
        
        for _ in range(32):
            dist += xor & 1
            xor >>= 1
            
        return dist