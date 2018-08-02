class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # idea: dynamic programming
        # the max is either everything from 0 to i or i

        # base cases
        if (nums is None or len(nums) == 0):
            return 0

        global_max = nums[0]
        current_max = nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            if (current_max > global_max):
                global_max = current_max


        return global_max
