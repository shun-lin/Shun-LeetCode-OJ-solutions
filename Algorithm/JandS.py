class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        if (J is None or len(J) == 0):
            return 0

        jewels = set()
        for jewel in J:
            jewels.add(jewel)

        numJewelsInS = 0

        for stone in S:
            if stone in jewels:
                numJewelsInS += 1

        return numJewelsInS
