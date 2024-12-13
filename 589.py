	traversal = list()
    
    if root:
        traversal.append(root.val)
        for child in root.children:
            traversal += self.preorder(child)
    
    return traversal