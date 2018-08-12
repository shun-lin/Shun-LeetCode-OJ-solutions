class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        uniqueDigits = [0] * 11

        for i in range(0, 11):
            if (i == 0):
                uniqueDigits[i] = 1
            elif (i == 1):
                uniqueDigits[i] = 10
            else:
                lastDigitUnique = uniqueDigits[i-1] - uniqueDigits[i-2]
                uniqueDigits[i] = (lastDigitUnique * (10 - (i - 1))) + uniqueDigits[i-1]
            if (n == i):
                return uniqueDigits[i]

        if (n < len(uniqueDigits)):
            return uniqueDigits[n]
        return uniqueDigits[-1]
