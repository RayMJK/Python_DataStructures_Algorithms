class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        mapping = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in mapping:

                if stack:
                    top_one = stack.pop()
                else:
                    top_one = '#'

                if mapping[i] != top_one:
                    return False

            else:
                stack.append(i)

        if len(stack) == 0:
            return True
        else:
            return False
