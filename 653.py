
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr=[]
        def inorder(troot):
            nonlocal arr
            if not troot:
                return 
            inorder(troot.left)
            arr.append(troot.val)
            inorder(troot.right)
        inorder(root)
        x,y=0,len(arr)-1
        while(x<y):
            if(arr[x]+arr[y]<k):
                x+=1
            elif(arr[x]+arr[y]>k):
                y-=1
            elif(arr[x]+arr[y]==k):
                return True
        return False
        