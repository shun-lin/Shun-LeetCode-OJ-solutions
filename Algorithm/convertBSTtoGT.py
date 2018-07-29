# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # BST so that all nodes in the right are greater
        # Ideal runtime: O(n)
        # Assumption: we can modify the original tree

        # helper function for converting BST
        # inplace modifying root into Greater Tree
        # return the sum of root before update
        # pass down the value of the parent
        # if we are going to the right child, we don't need to pass in parent value as it will be smaller and not affecting
        # if we are going to the left child, we need to pass in parent value
        def helper(root, parent_val):
            # base case
            if (root is None):
                return 0

            result = root.val
            root.val += parent_val

            if (root.left is None and root.right is None):
                return result

            if (root.right):
                sum_of_right = helper(root.right, parent_val)
                root.val += sum_of_right
                result += sum_of_right

            if (root.left):
                result += helper(root.left, root.val)

            return result

        # we do not need the return value
        # no parent, so pass in 0 as parent_val
        helper(root, 0)
        return root
