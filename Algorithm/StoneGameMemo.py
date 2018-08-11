class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        # memorization for the state of recurrsion relationship
        # the state is (currentPlayerScore, opponentPlayerScore, start, end)
        memo = dict()

        totalPossibleScores = sum(piles)

        # return true if the current player can win, false other wise
        # currentPlayerScore, score of current player
        # opponentPlayerScore, score of opponent player
        # start: start of the rest of piles, inclusive
        # end: end of the rest of piles, not inclusive
        def helper(currentPlayerScore, opponentPlayerScore, start, end):

            key = (currentPlayerScore, opponentPlayerScore, start, end)
            if key in memo:
                return memo[key]

            if (currentPlayerScore > totalPossibleScores / 2):
                memo[key] = True
                return True
            elif (opponentPlayerScore > totalPossibleScores / 2):
                memo[key] = False
                return False

            # base case
            if (start >= end):
                result = currentPlayerScore > opponentPlayerScore
                memo[key] = result
                return result

            leftMostStone = piles[start]
            rightMostStone = piles[end - 1]

            opponentWinIfTakeLeft = helper(opponentPlayerScore, currentPlayerScore + leftMostStone, start + 1, end)

            if not opponentWinIfTakeLeft:
                memo[key] = True
                return True

            opponentWinIfTakeRight = helper(opponentPlayerScore, currentPlayerScore + rightMostStone, start, end -1)

            if not opponentWinIfTakeRight:
                memo[key] = True
                return True

            memo[key] = False
            return False

        return helper(0, 0, 0, len(piles))
