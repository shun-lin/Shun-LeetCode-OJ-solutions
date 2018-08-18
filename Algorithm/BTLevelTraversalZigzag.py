# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        def helper(root, level):
            if root == None:
                return

            if (level >= len(result)):
                result.append([])
            result[level].append(root.val)

            helper(root.left, level + 1)
            helper(root.right, level + 1)


        helper(root, 0)
        for i in range(1, len(result), 2):
            result[i] = list(reversed(result[i]))

        return result
