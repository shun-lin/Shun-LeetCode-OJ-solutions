# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # helper function that returns tile and sum
        def helper(root):
            tile_of_tree = 0
            sum_of_tree = 0

            if (root is None):
                return 0, 0

            tile_of_left, sum_of_left = helper(root.left)
            tile_of_right, sum_of_right = helper(root.right)

            tile_of_tree = abs(sum_of_left - sum_of_right) + tile_of_left + tile_of_right
            sum_of_tree = sum_of_left + sum_of_right + root.val

            return tile_of_tree, sum_of_tree

        tile_of_tree, sum_of_tree = helper(root)
        return tile_of_tree
