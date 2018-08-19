class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        winningHash = dict()
        # states: remainingTotal and set of selectable integers

        def helper(selectables, remainingTotal):
            key = tuple(selectables)

            if key in winningHash:
                return winningHash[key]

            if (len(selectables) == 0 and remainingTotal > 0):
                winningHash[key] = False
                return False

            for selectable in selectables:
                remainingSelectables = selectables.copy()
                remainingSelectables.remove(selectable)
                if (remainingTotal - selectable <= 0 or not helper(remainingSelectables, remainingTotal - selectable)):
                    winningHash[key] = True
                    return True
            winningHash[key] = False
            return False

        originalSelectables = set()
        sumOfSelectables = 0
        for i in range(1, maxChoosableInteger + 1):
            originalSelectables.add(i)
            sumOfSelectables += i

        return sumOfSelectables >= desiredTotal and helper(originalSelectables, desiredTotal)
