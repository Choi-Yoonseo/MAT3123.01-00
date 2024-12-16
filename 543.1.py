

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter  = 0
        stack = [(root, False)]
        dictionary = {}

        while stack:
            currentNode, visited = stack.pop()
            if not currentNode : continue

            # Confused? You should be but it's Very simple. 
            # You pop a node. isn't it Cool!
            # That node will have a left and right node. You agree?
            # We are checking in the dictionary whether we  have visited that node already. 
            # If so, we would have stored the longest path in the dictionary. 
            # If not, we return 0 for that side, i.e., the left or right side longest path.
            # Whatever the dictionary returns, we add them to get our new diameter. If that diameter is bigger than the current, we update.
            # Lastly, we store the currentNode into the dictionary too, 
            # because,  It might be the left or right node of a parent node. Since We are using a bottom-up approach.

            if visited:
                left = dictionary.get(currentNode.left , 0)
                right = dictionary.get(currentNode.right , 0)
                diameter = max(diameter, left + right)
                dictionary[currentNode] = 1 + max(left, right)
            else:
                stack.append((currentNode, True))
                stack.append((currentNode.right, False))
                stack.append((currentNode.left, False))
      
        return diameter