class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)

        # running_sum is a list
        self.running_sum = dict()
        self.running_sum[-1] = 0
        for i in range(n):
            last_sum = self.running_sum[i - 1]
            self.running_sum[i] = last_sum + nums[i]


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.running_sum[j] - self.running_sum[i - 1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
