class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True

        scores = dict()

        # return the best score
        # if it is playerOne's turn (isPlayerOne == True), want to maximize score
        # minimize otherwise (isPlayerOneMultiplier == False)
        # start is inclusive, end is not inclusive
        def helper(start, end, currentScore, isPlayerOne):

            # base case
            if (start >= end):
                return currentScore
            # only one choice
            elif (start == end - 1):
                if (isPlayerOne):
                    return currentScore + nums[start]
                else:
                    return currentScore - nums[start]
            else:
                if (isPlayerOne):
                    takenLeftCurrentScore = currentScore + nums[start]
                    takenLeftTotalScore = helper(start + 1, end, takenLeftCurrentScore, False)
                    takenRightCurrentScore = currentScore + nums[end - 1]
                    takenRightTotalScore = helper(start, end - 1, takenRightCurrentScore, False)
                    return max(takenLeftTotalScore, takenRightTotalScore)
                else:
                    takenLeftCurrentScore = currentScore - nums[start]
                    takenLeftTotalScore = helper(start + 1, end, takenLeftCurrentScore, True)
                    takenRightCurrentScore = currentScore - nums[end - 1]
                    takenRightTotalScore = helper(start, end - 1, takenRightCurrentScore, True)
                    return min(takenLeftTotalScore, takenRightTotalScore)



        return helper(0, len(nums), 0, True) >= 0
