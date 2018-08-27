# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # key will be N and the value will be the solution to allPossbileFBT
    hashed = dict()
    
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        # if it is even, return empty list as it is impossible
        if N % 2 == 0:
            return []
        
        if N in self.hashed:
            return self.hashed[N]
        
        result = []
        
        # base case
        if N == 1:
            result.append(TreeNode(0))
            self.hashed[N] = result
            return result
        
        for i in range(1, N - 1, 2):
            leftFBTs = self.allPossibleFBT(i)
            rightFBTs = self.allPossibleFBT(N - i - 1)
            
            for leftFBT in leftFBTs:
                for rightFBT in rightFBTs:
                    onePossibleFTB = TreeNode(0)
                    onePossibleFTB.left = leftFBT
                    onePossibleFTB.right = rightFBT
                    result.append(onePossibleFTB)
        
        self.hashed[N] = result
        return result
        
            