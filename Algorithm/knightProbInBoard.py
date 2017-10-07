class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        # reursion with memo approach
        memo = dict();
        def helper(N, K, r, c):
            # this position is out of bound
            if (r < 0 or r > N - 1 or c < 0 or c > N - 1):
                return 0;
            if (K == 0):
                return 1;
            key = (K, r, c);
            if (key in memo):
                return memo[key];
            else:
                upLeft = helper(N, K - 1, r - 2, c - 1)
                leftUp = helper(N, K - 1, r - 1, c - 2)
                downLeft = helper(N, K - 1, r + 2, c - 1)
                leftDown = helper(N, K - 1, r + 1, c - 2)
                upRight = helper(N, K - 1, r - 2, c + 1)
                rightUp = helper(N, K - 1, r - 1, c + 2)
                downRight = helper(N, K - 1, r + 2, c + 1)
                rightDown = helper(N, K - 1, r + 1, c + 2)
                result = float(upLeft + leftUp + downLeft + leftDown + upRight + rightUp + downRight + rightDown) / 8
                memo[key] = result
                return result

        return helper(N, K, r, c);
