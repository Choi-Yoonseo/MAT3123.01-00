class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def recurse(l, r):
            # base case, l must always be <= r
            # l == r is the case of a leaf node.
            if l > r: return None
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = recurse(l, mid-1)
            node.right = recurse(mid+1, r)
            return node
        # both the indices are inclusive,
        # mathematically given by: [0, len(nums)-1]
        return recurse(0, len(nums)-1)