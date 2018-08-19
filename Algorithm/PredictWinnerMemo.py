class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True

        scores = dict()

        # return the best score for what is left between start and end
        # always true to  want to maximize score
        # start is inclusive, end is not inclusive
        def helper(start, end):
            key = (start, end)
            if key in scores:
                return scores[key]

            # initialize result
            result = 0

            # base case
            if (start >= end):
                result = 0
            # only one choice
            elif (start == end - 1):
                result = nums[start]
            else:
                takenLeftTotalScore = nums[start] - helper(start + 1, end)
                takenRightTotalScore = nums[end - 1] - helper(start, end - 1)
                result = max(takenLeftTotalScore, takenRightTotalScore)

            # store score and return result
            scores[key] = result
            return result



        return helper(0, len(nums)) >= 0
