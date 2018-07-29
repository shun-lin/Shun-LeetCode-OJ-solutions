"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result = []

        # helper function that takes in three parameters
        # root, the level of root, and result list of lists
        def helper(root, root_level, result):
            if (root is None):
                return
            if (len(result) <= root_level):
                result.append([])
            result[root_level].append(root.val)

            for child in root.children:
                helper(child, root_level + 1, result)


        helper(root, 0, result)
        return result
