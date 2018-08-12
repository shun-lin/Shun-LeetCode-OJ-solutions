class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # assumption: n is greater than 1
        maxProduct = [0] * (n + 1)

        for i in range(n+1):
            if (i <= 1):
                maxProduct[i] = i
            elif (i == 2):
                maxProduct[i] = 1
            else:
                currMaxProd = 0
                for j in range(0, i / 2 + 1):
                    k = i - j
                    prod = max(j, maxProduct[j]) * max(k, maxProduct[k])
                    currMaxProd = max(currMaxProd, prod)
                maxProduct[i] = currMaxProd

        return maxProduct[n]
