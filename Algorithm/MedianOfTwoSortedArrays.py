# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2;
        nums.sort();
        if (len(nums) % 2 != 0):
            return nums[len(nums) / 2];
        else:
            return float((nums[len(nums) / 2 - 1] + nums[len(nums) / 2])) / 2;
