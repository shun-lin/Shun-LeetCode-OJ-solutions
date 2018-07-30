# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # base case
        if (root is None):
            return None

        left_child = self.pruneTree(root.left)
        right_child = self.pruneTree(root.right)

        if (not left_child and not right_child and root.val == 0):
            return None

        root.left = left_child
        root.right = right_child

        return root
