class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        for i in range(len(arr) - 2):
            a = arr[i]
            b = arr[i + 1]
            c = arr[i + 2]

            if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
                return True

        return False