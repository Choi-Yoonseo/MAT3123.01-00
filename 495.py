# BF TLE 21/40
#
# AC!
class Solution:

    def findPoisonedDuration(self, t: List[int], duration: int) -> int:
        ans = 0

        # first start and end
        start = t[0]
        end = start + duration  # end is the first time not poisoned

        # if new poisining is an extension of current one, extends end
        # otherwise we will have a new period of poisoning
        for i in range(1, len(t)):

            if t[i] <= end:
                end = t[i] + duration   # new end
            else:
                ans += end - start
                start = t[i]            # new start and end
                end = start + duration
            
        # last poisoning
        ans += end - start

        return ans

    def findPoisonedDuration_BF(self, timeSeries: List[int], duration: int) -> int:
        
        p = set()

        for t in timeSeries:
            for d in range(duration):
                p.add(t+d)

        return len(p)