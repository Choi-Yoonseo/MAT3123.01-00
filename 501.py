# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = Counter()

        def recur(node):
            if not node:
                return
            counts[node.val] += 1
            recur(node.left)
            recur(node.right)

        recur(root)
        res = []
        maxCount = 0
        for i in counts:
            if counts[i] == maxCount:
                res.append(i)
            elif counts[i] > maxCount:
                maxCount = counts[i]
                res.clear()
                res.append(i)
        return res