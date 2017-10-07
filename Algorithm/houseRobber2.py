class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # using dynamic programming approach
        if len(nums) <= 0:
            return 0;
        if (len(nums) == 1):
            return nums[0];
        dp = [0] * len(nums);
        for i in range(0, len(nums)):
            if (i == 0):
                dp[i] = nums[i];
            elif (i == 1):
                dp[i] = max(nums[i], dp[i - 1]);
            elif (i == 2):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1]);
            else:
                max_with_arr_i = nums[i] + max(dp[i - 2], dp[i - 3]);
                dp[i] = max(dp[i - 1], max_with_arr_i);

        dp_without_first = [0] * len(nums);
        for i in range(0, len(nums)):
            if (i == 0):
                dp_without_first[i] = 0;
            elif (i == 1):
                dp_without_first[i] = max(nums[i], dp_without_first[i - 1]);
            elif (i == 2):
                dp_without_first[i] = max(nums[i] + dp_without_first[i - 2], dp_without_first[i - 1]);
            else:
                max_with_arr_i = nums[i] + max(dp_without_first[i - 2], dp_without_first[i - 3]);
                dp_without_first[i] = max(dp_without_first[i - 1], max_with_arr_i);

        return max(dp[-2], dp_without_first[-1]);
