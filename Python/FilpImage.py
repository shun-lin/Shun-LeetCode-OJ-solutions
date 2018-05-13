class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # revert rows
        for i in range(len(A)):
            for j in range(len(A[i]) / 2):
                temp = A[i][j]
                A[i][j] = 1 - A[i][-j-1]
                A[i][-j-1] = 1 - temp
            if (len(A[i]) % 2 != 0):
                A[i][len(A[i]) / 2] = 1 - A[i][len(A[i]) / 2]
        return A
