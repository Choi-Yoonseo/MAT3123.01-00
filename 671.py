# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # l=sl=float('inf')
        # def dfs(root):
        #     nonlocal l
        #     nonlocal sl
        #     if not root:
        #         return
        #     if root.val<l:
        #         sl=l
        #         l=root.val
        #     elif root.val<sl and root.val>l:
        #         sl=root.val
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return sl if sl!=float('inf') else -1

        def dfs(root):
            if not root:
                return -1
            if not root.left and not root.right:
                return -1
            l,r=root.left.val,root.right.val
            if root.left.val==root.val: l=dfs(root.left)
            if root.right.val==root.val: r=dfs(root.right)
            if l!=-1 and r!=-1:
                return min(l,r)
            if l!=-1:
                return l
            return r
        return dfs(root)