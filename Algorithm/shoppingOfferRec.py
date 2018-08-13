import numpy

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        memo = dict()

        # key is the tuple of specials, value is the price
        specialDict = dict()
        for offer in special:
            items = tuple(offer[0:len(offer) - 1])
            cost = offer[-1]
            if items in specialDict:
                specialDict[items] = min(specialDict[items], cost)
            else:
                specialDict[items] = cost

        def helper(needsTuple):
            if needsTuple in memo:
                return memo[needsTuple]

            for need in needsTuple:
                if (need < 0):
                    result = 10000000
                    memo[needsTuple] = result
                    return result


            currentMin = 0
            for i in range(0, len(needsTuple)):
                currentMin += price[i] * needsTuple[i]

            for offer in specialDict:
                needsAfterUsingOffer = tuple(numpy.subtract(needsTuple, offer))
                currentMin = min(currentMin, helper(needsAfterUsingOffer) + specialDict[offer])

            memo[needsTuple] = currentMin
            return int(currentMin)

        return helper(tuple(needs))
