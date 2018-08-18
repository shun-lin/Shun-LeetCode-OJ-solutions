# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (not root):
            return 0
        # this fringe will hold a list of tuple (node, depth)
        fringe = []
        rootElement = (root, 1)
        fringe.append(rootElement)

        while len(fringe) > 0:
            visitingNode, depth = fringe.pop(0)
            if (visitingNode.left == None and visitingNode.right == None):
                return depth
            if (visitingNode.left != None):
                fringe.append((visitingNode.left, depth + 1))
            if  (visitingNode.right != None):
                fringe.append((visitingNode.right, depth + 1))
