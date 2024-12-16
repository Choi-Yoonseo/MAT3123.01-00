def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): 
        return None
    result = []
    while number > 0:
        result.append(digits[number % base])
        number //= base
    result = ''.join(reversed(result))
    return result.upper() if upper else result
    
class Solution:
    def findComplement(self, num: int) -> int:
        num_2 = convert_to(num, 2)
        num_2_complement = num_2.replace('0', 'x').replace('1','0').replace('x', '1')
        return int(num_2_complement, 2)