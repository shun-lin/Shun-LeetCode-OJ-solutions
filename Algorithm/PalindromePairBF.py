class Solution(object):

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def reverse(s):
            if (s == None or len(s) == 0):
                return s;
            result = "";
            for i in range(len(s) - 1, -1, -1):
                result += s[i];
            return result;

        def isPalindrome(s):
            if (s == None or len(s) == 0):
                return True;
            else:
                start = 0;
                end = len(s) - 1;
                while (start < end):
                    if (s[start] != s[end]):
                        return False;
                    start += 1;
                    end -= 1;
                return True;

        if (words == None or len(words) == 0):
            return [];
        result = [];
        for i in range(len(words)):
            for j in range(len(words)):
                if (i != j):
                    if (isPalindrome(words[i] + words[j])):
                        result.append([i, j]);
        return result;
