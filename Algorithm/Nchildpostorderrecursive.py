"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # recursive approach
        result = []
        if (root is None):
            return result

        for child in root.children:
            result.extend(self.postorder(child))

        result.append(root.val)

        return result
