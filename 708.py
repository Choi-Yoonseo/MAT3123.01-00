# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res=float('inf')
        pre=-1
        def tree(root):
            nonlocal res
            nonlocal pre
            if not root:
                return 
            tree(root.left)
            if pre!=-1:
                res=min(res,root.val-pre)
            pre=root.val
            tree(root.right)
        tree(root)
        return res