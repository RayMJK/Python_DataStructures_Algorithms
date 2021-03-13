class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        result = []

        def backtrack(i, cur_str):
            if len(cur_str) == len(digits):
                result.append(cur_str)
                return
            for c in phone[digits[i]]:
                backtrack(i + 1, cur_str + c)

        if digits:
            backtrack(0, "")

        return result