# This code has run time of O(n) and space usage of O(1)

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums);
        slow = 0;
        fast = 0;
        finder = 0;
        while (True):
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast):
                break;
        while (True):
            slow = nums[slow];
            finder = nums[finder];
            if (slow == finder):
                return slow;
