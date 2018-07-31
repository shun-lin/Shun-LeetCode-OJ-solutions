class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        # 0 -> 0    0
        # 1 -> 1    1
        # 2 -> 10    1
        # 3 -> 11    2
        # 4 -> 100   1
        # 5 -> 101   2
        # 6 -> 110   2
        # 7 -> 111   3
        # 8 -> 1000  1
        # 9 -> 1001  2
        # 10 -> 1010 2
        # 11 -> 1011 3
        # 12 -> 1100 2
        # 13 -> 1101 3
        # 14 -> 1110 3
        # 15 -> 1111 4

        # rules: base case will be 0 and 1, when it is odd, add 1 bit to the number of bits before
        # When it is even, we need to know how many bits we have erased and then plus one more, we can store the number of bits represented and the next int we need to increase our bit represented by one

        biggest_power_of_two_so_far = 1

        result = []

        for i in range(num + 1):

            # base cases
            if (i <= 1):
                result.append(i)
            elif (i == biggest_power_of_two_so_far * 2):
                biggest_power_of_two_so_far *= 2
                result.append(1)
            else:
                result.append(result[i - biggest_power_of_two_so_far] + 1)

        return result
