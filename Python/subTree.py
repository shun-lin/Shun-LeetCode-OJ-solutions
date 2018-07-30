# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        # helper function that takes in s, t, and t_root where t_root is the subtree that must match from the root
        # return tree is either t is a subtree of s or t_root is a subtree at root of s
        def helper(s, t_original, t_root):

            # base case
            if (s is None and t_original is None):
                return True

            if (s is None and t_root is None):
                return True

            if (t_original is None):
                return True

            if (s is None):
                return False

            t_root_result = False
            t_original_result = False
            if (not t_root is None and s.val == t_root.val):
                t_root_result = helper(s.left, t_original, t_root.left) and helper(s.right, t_original, t_root.right)
                if (t_root_result):
                    return True
            if (s.val == t_original.val):
                t_original_result = helper(s.left, t_original, t_original.left) and helper(s.right, t_original, t_original.right)
                if (t_original_result):
                    return True
            return helper(s.left, t_original, t_original) or helper(s.right, t_original, t_original)


        return helper(s, t, t)
