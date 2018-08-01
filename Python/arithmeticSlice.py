class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # to uniquely identify an arithmetic slice in A, we need p and q, and this arithmetic slice as a common difference of d
        # idea: we can find all the shortest slices, length of 3, and use them to find number of slices with length of 4, so on until length of the whole, another approach is to find the longnest running slice and do math

        # 3 -> 1
        # 4 -> 2 + 1
        # 5 -> 3 + 2 + 1
        # 6 -> 4 + 3 + 2 + 1

        # num_arithmetic_storage[i] = (i - 2)  + num_arithmetic_storage[i - 1]

        count = 0
        ran_length = 0
        difference = 0
        highest_stored_value = 3
        num_arithmetic_storage = dict()
        num_arithmetic_storage[0] = 0
        num_arithmetic_storage[1] = 0
        num_arithmetic_storage[2] = 0
        num_arithmetic_storage[3] = 1

        if (A is None or len(A) < 3):
            return 0

        for i in range(len(A) - 1):
            if (i == 0):
                difference = A[i + 1] - A[i]
                ran_length = 2
            else:
                new_difference = A[i + 1] - A[i]
                if (new_difference == difference):
                    ran_length += 1
                    continue
                while(ran_length > highest_stored_value):
                    highest_stored_value += 1
                    num_arithmetic_storage[highest_stored_value] = (highest_stored_value -2) + num_arithmetic_storage[highest_stored_value - 1]
                count += num_arithmetic_storage[ran_length]
                ran_length = 2
                difference = new_difference

        if (ran_length >= 3):
            while(ran_length > highest_stored_value):
                    highest_stored_value += 1
                    num_arithmetic_storage[highest_stored_value] = (highest_stored_value -2) + num_arithmetic_storage[highest_stored_value - 1]
            count += num_arithmetic_storage[ran_length]

        return count
