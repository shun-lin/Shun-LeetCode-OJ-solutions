#  Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#   You may assume that each input would have exactly one solution

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0;
        j = 1;
        sum = nums[0] + nums[1];
        while (target != sum):
            if (j == len(nums) - 1):
                i += 1;
                j = i + 1;
            else:
                j += 1;
            sum = nums[i] + nums[j];
        return [i, j];
