"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        # base case
        if (quadTree1 is None and quadTree2 is None):
            return None

        # initialize a empty QuadTree result
        result = Node(False, True, None, None, None, None)

        if (quadTree1.isLeaf and quadTree2.isLeaf):
            result.val = quadTree1.val or quadTree2.val
        elif (quadTree1.isLeaf):
            if (quadTree1.val):
                result.val = True
            else:
                result.isLeaf = False
                result.topLeft = quadTree2.topLeft
                result.topRight = quadTree2.topRight
                result.bottomLeft = quadTree2.bottomLeft
                result.bottomRight = quadTree2.bottomRight
        elif (quadTree2.isLeaf):
            if (quadTree2.val):
                result.val = True
            else:
                result.isLeaf = False
                result.topLeft = quadTree1.topLeft
                result.topRight = quadTree1.topRight
                result.bottomLeft = quadTree1.bottomLeft
                result.bottomRight = quadTree1.bottomRight
        else:
            result.isLeaf = False
            result.topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            result.topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            result.bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            result.bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        if (not result.isLeaf and result.topLeft.isLeaf and result.topRight.isLeaf and result.bottomLeft.isLeaf and result.bottomRight.isLeaf and result.topLeft.val == result.topRight.val and result.topLeft.val == result.bottomLeft.val and result.topLeft.val == result.bottomRight.val):
            result = Node(result.topLeft.val, True, None, None, None, None)

        return result
        
