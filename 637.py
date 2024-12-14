# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        s=defaultdict(int)
        n=defaultdict(int)
        def dfs(root,depth):
            s[depth]+=root.val
            n[depth]+=1
            if root.left: dfs(root.left,depth+1)
            if root.right: dfs(root.right,depth+1)
        dfs(root,0)
        ar=[]
        for i in s.keys():
            ar.append(s[i]/n[i])
        return ar