# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        # base case
        if (nums is None or len(nums) == 0):
            return None

        max_number = max(nums)
        max_index = nums.index(max_number)

        result = TreeNode(max_number)
        result.left = self.constructMaximumBinaryTree(nums[0:max_index])
        result.right = self.constructMaximumBinaryTree(nums[max_index + 1:len(nums)])

        return result
