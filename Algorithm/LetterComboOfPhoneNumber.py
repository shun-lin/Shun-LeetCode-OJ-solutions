class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if (digits == None or len(digits) == 0):
            return [];

        letters = dict();
        letters['1'] = "";
        letters['2'] = "abc";
        letters['3'] = "def";
        letters['4'] = "ghi";
        letters['5'] = "jkl";
        letters['6'] = "mno";
        letters['7'] = "pqrs";
        letters['8'] = "tuv";
        letters['9'] = "wxyz";

        result = [];
        for number in digits:
            str_of_letters = letters[number];
            if (len(result) == 0):
                for character in str_of_letters:
                    result.append(character);
            else:
                new_result = [];
                for before_str in result:
                    for new_letter in str_of_letters:
                        new_result.append(before_str + new_letter);
                result = new_result;
        return result;
