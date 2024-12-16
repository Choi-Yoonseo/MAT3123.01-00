class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # USe the empty space first, start filling from the back
        insertHere = (m+n)-1

        i, j = m-1, n-1
        while (i>=0 and j>=0):
            if nums1[i]>=nums2[j]:
                nums1[insertHere]=nums1[i]
                i -= 1
            else:
                nums1[insertHere]=nums2[j]
                j -= 1
            insertHere -= 1
        
        # Fill the remaining elements
        if i>=0 and j<0:
            while(i>=0):
                nums1[insertHere]=nums1[i]
                i -= 1
                insertHere -= 1

        if j>=0 and i<0:
            while(j>=0):
                nums1[insertHere]=nums2[j]
                j -= 1
                insertHere -= 1

