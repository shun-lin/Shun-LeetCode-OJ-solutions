class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        
        # the key is the length of the words
        # and the value is a set of words
        wordsDict = dict()
        for word in d:
            key = len(word)
            if key not in wordsDict:
                wordsDict[key] = set()
            wordsDict[key].add(word)
        
        visited = set()
        
        # BST approach
        fringe = []
        fringe.append(s)
        
        results = []
        resultLength = 0
        while len(fringe) > 0:
            visiting = fringe.pop(0)
            if resultLength > len(visiting):
                break

            if visiting in visited:
                continue
            
            key = len(visiting)
            if key in wordsDict and visiting in wordsDict[key]:
                results.append(visiting)
                resultLength = key
            
            for i in range(len(visiting)):
                # remove index i from visiting
                toVisit = visiting[:i] + visiting[i+1:]
                fringe.append(toVisit)

            visited.add(visiting)
        
        return min(results)