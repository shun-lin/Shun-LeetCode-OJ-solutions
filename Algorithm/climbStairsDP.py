class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [0] * (n+1)

        for i in range(n+1):
            if (i <= 2):
                ways[i] = i
            else:
                ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]
