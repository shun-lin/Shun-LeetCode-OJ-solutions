# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # runtime: O(n) where n is the number of nodes of the bigger tree of the two
        # base case
        if (t1 is None and t2 is None):
            return None

        root_value = 0
        if (t1 is None):
            root_value = t2.val
            result_tree = TreeNode(root_value)
            result_tree.left = self.mergeTrees(None, t2.left)
            result_tree.right = self.mergeTrees(None, t2.right)
        elif (t2 is None):
            root_value = t1.val
            result_tree = TreeNode(root_value)
            result_tree.left = self.mergeTrees(t1.left, None)
            result_tree.right = self.mergeTrees(t1.right, None)
        else:
            root_value = t2.val + t1.val
            result_tree = TreeNode(root_value)
            result_tree.left = self.mergeTrees(t1.left, t2.left)
            result_tree.right = self.mergeTrees(t1.right, t2.right)

        return result_tree
