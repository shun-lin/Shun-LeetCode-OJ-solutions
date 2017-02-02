# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.

# You can only see the k numbers in the window. Each time the sliding window moves right by one position.

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return nums;
        result_length = len(nums) - k + 1;
        result = [0] * result_length;
        i = 0;
        while i < result_length:
            ind_max = max(nums[i: i + k]);
            result[i] = ind_max;
            i += 1;
        return result;
