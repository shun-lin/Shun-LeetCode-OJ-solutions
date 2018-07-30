# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # helper function that returns two values
        # whether it is balance and the depth
        def helper(root):

            # base case
            if (root is None):
                return True, 0

            balanced_left, depth_left = helper(root.left)
            balanced_right, depth_right = helper(root.right)

            depth = 1 + max(depth_left, depth_right)
            balanced = abs(depth_left - depth_right) <= 1 and balanced_left and balanced_right

            return balanced, depth


        balanced, _depth = helper(root)
        return balanced
