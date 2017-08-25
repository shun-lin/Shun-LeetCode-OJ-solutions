class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s, start, end):
            if (s == None or len(s) == 0):
                return True;
            else:
                while (start < end):
                    if (s[start] != s[end]):
                        return False;
                    start += 1;
                    end -= 1;
                return True;
        def reverse(s):
            if (s == None or len(s) == 0):
                return s;
            result = "";
            for i in range(len(s) - 1, -1, -1):
                result += s[i];
            return result;

        if (s == None or len(s) == 0):
            return s;
        for i in range(len(s) - 1, -1, -1):
            if (isPalindrome(s, 0, i)):
                break;
        toAdd = reverse(s[i+1:len(s)]);
        return toAdd + s;
