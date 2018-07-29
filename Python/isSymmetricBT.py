# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def createMirror(root):
            if (root is None):
                return None
            result = TreeNode(root.val)
            result.left = createMirror(root.right)
            result.right = createMirror(root.left)
            return result

        def isSameBT(p, q):
            if (p is None and q is None):
                return True

            if (p is None or q is None):
                return False

            return p.val == q.val and isSameBT(p.left, q.left) and isSameBT(p.right, q.right)

        if (root is None):
            return True

        expected_right = createMirror(root.left)
        return isSameBT(expected_right, root.right)
