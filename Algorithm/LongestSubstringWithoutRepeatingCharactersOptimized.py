class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def initialize_storage(s, storage):
            for char in s:
                storage[char] = -1;

        if s == None or len(s) == 0:
            return 0;
        storage = dict();
        initialize_storage(s, storage);
        start = 0;
        current_max = 0;
        temp_max = 0;
        for i in range(0, len(s)):
            char = s[i];
            index = storage[char];
            if (index == -1 or index < start):
                temp_max += 1;
            else:
                temp_max -= index - start;
                start = index + 1;
            storage[char] = i;
            if (temp_max > current_max):
                current_max = temp_max;
        return current_max
