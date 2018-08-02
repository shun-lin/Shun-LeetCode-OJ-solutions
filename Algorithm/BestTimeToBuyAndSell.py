class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # we want differences, buy low and sell high

        currentLow = 0
        globalProfit = 0

        if (prices is None or len(prices) <= 1):
            return 0

        for i in range(len(prices)):
            if (i == 0):
                currentLow = prices[i]
            else:
                profit = prices[i] - currentLow
                if (profit > globalProfit):
                    globalProfit = profit
                if (prices[i] < currentLow):
                    currentLow = prices[i]

        return globalProfit
