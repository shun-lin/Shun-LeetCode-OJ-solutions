# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # helper function that returns longest diameter that pass through root
        # and longest diameter that does not pass through root
        # and the depth of tree
        def helper(root):
            # base case
            if (root is None):
                return 0, 0, 0

            left_diameter_through_root, left_diameter_not_through_root, left_depth = helper(root.left)
            right_diameter_through_root, right_diameter_not_through_root, right_depth = helper(root.right)

            diameter_not_through_root = max(left_diameter_through_root, left_diameter_not_through_root, right_diameter_through_root, right_diameter_not_through_root)

            diameter_through_root = 0
            if (root.left):
                diameter_through_root += left_depth
            if (root.right):
                diameter_through_root += right_depth

            depth = 1 + max(left_depth, right_depth)

            return diameter_through_root, diameter_not_through_root, depth

        diameter_through_root, diameter_not_through_root, tree_depth = helper(root)
        return max(diameter_through_root, diameter_not_through_root)
