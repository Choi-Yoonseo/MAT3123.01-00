# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.left is None and root.right is None:
            return [str(root.val)]
        def findpath(node,l,L):
            if node.left is None and node.right is None:
                l += str(node.val)
                L.append(l)
            if node.left is not None:
                findpath(node.left,l+str(node.val)+"->",L)
            if node.right is not None:
                findpath(node.right,l+str(node.val)+"->",L)
            return L      
       
        return findpath(root,"",[])


            