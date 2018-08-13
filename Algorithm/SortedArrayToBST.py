# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        middleIndex = len(nums) / 2
        result = TreeNode(nums[middleIndex])
        leftSubTree = self.sortedArrayToBST(nums[:middleIndex])
        rightSubTree = self.sortedArrayToBST(nums[middleIndex + 1:])

        result.left = leftSubTree
        result.right = rightSubTree

        return result
