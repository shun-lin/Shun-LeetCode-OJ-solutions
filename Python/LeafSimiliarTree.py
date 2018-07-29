# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        # idea: need to use in order
        # runtime: O(n)

        def LeafSequence(root):
            result = []
            if (root is None):
                return result
            left_leaf_sequence = LeafSequence(root.left)
            right_leaf_sequence = LeafSequence(root.right)
            if (len(left_leaf_sequence) == 0 and len(right_leaf_sequence) == 0):
                result.append(root.val)
            else:
                result.extend(left_leaf_sequence)
                result.extend(right_leaf_sequence)
            return result

        root_1_leaf_sequence = LeafSequence(root1)
        root_2_leaf_sequence = LeafSequence(root2)

        if (len(root_1_leaf_sequence) != len(root_2_leaf_sequence)):
            return False

        for i in range(len(root_1_leaf_sequence)):
            if (root_1_leaf_sequence[i] != root_2_leaf_sequence[i]):
                return False

        return True
