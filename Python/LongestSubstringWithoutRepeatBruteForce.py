class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(s, index):
            temp_storage = dict();
            max_length = 0;
            for i in range(index, len(s)):
                if s[i] in temp_storage:
                    return max_length;
                temp_storage[s[i]] = True;
                max_length += 1;
            return max_length;

        if s == None or len(s) == 0:
            return 0;
        max_length = 0;
        for i in range(0, len(s)):
            temp_max = helper(s, i)
            if (temp_max > max_length):
                max_length = temp_max;
        return max_length;
