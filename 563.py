class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """
        Given the root to a binary tree, this program determines
        the tilt of the tree. In order to compute the tilt, this
        program recursively computes the sum of the nodes in each
        subtree.

        :param root: root to a binary tree
        :type root: TreeNode
        :return: tilt value of binary tree
        :rtype: int
        """
        self.tilt = 0

        def compute_sum(root: TreeNode) -> int:
            """
            This program recursively computes the sum of each
            subtree in the tree passed to this program.  It uses
            the subtree sums to determine the tilt of the tree.

            :param root: root to a tree or subtree
            :type root: TreeNode
            :return: subtree sum
            :rtype: int
            """
            if root == None:
                return 0
            left_sum = compute_sum(root.left)
            right_sum = compute_sum(root.right)
            self.tilt += abs(left_sum - right_sum)
            tree_sum = left_sum + root.val + right_sum
            return tree_sum

        compute_sum(root)
        return self.tilt