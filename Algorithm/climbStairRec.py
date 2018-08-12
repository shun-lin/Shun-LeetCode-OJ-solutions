class Solution(object):
    memo = dict()
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo:
            return self.memo[n]

        if (n <= 2):
            return n

        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = result
        return result
