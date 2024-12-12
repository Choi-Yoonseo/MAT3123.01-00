class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1 or 1 not in bits: return True
        if len(bits) == 2:
            if bits[0] == 1: return False
            return True
        
        i = 0
        while i < len(bits)-1:
            if bits[i] == 0:
                i += 1
            elif bits[i] == 1:
                i += 2

        return False if i == len(bits) else True