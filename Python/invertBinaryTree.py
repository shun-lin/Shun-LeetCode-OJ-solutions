# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # runtime: O(n)
        # idea: inverting grandchildren first then children

        # base case
        if (root is None):
            return None

        result_tree = TreeNode(root.val)

        left_tree = self.invertTree(root.left)
        right_tree = self.invertTree(root.right)

        result_tree.left = right_tree
        result_tree.right = left_tree

        return result_tree
