class Solution(object):
    
    # key is K
    hashed = dict()
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        # brute force idea: use DP and iterate from 1 ... N and build the array
        # and then find the K element, this is both slow and mem consuming
        
        # assuming K exists in N, we know that K index comes from (N, K) comes from (N-1, K+1 // 2)
        # if K is even, we need to flip the bits from (N-1, K+1 // 2)
        # if K is odd, it is the same bit from (N-1, K+1 // 2)
        # base case when K is 1 or 2 then we return 0 and 1 respectively
        
        if K in self.hashed:
            return self.hashed[K]
        
        if K == 1:
            return 0
        elif K == 2:
            return 1
        
        needToFlip = K % 2 == 0
        result = self.kthGrammar(N-1, (K+1) // 2)
        if needToFlip:
            result = 1 - result
        self.hashed[K] = result
        return result