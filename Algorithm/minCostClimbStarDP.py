class Solution(object):

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        minCost = [0] * (len(cost) + 1)

        for i in range(len(cost) + 1):
            if (i <= 1):
                minCost[i] = 0
            else:
                minCost[i] = min(minCost[i - 1] + cost[i - 1], minCost[i - 2] + cost[i - 2])

        return minCost[-1]
