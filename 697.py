class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        def helper(n, nums):
            start, end = 0, 0
            for i in range(len(nums)):
                if nums[i] == n:
                    start = i
                    break
            
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == n:
                    end = i
                    break
            
            return [start, end]

         
        # count frequency of each character
        count = {}
        for i in nums:
            if not i in count:
                count[i] = 1
            else:
                count[i] += 1
        
        maxFreq = max(count.values())
        maxNum = []
        for i in count:
            if count[i] == maxFreq:
                maxNum.append(i)
        # start iterating from beginning and ending simultaneously
        # until you find the maxNum
        res = float('inf')
        for i in maxNum:
            start, stop = helper(i, nums)
            res = min(res, abs(stop - start) + 1) 
        
        return res



        


        

            
         
        

        

        
            
        
                
            
      