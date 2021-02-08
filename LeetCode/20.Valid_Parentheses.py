class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for i in s:
            if stack:
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                elif stack[-1] == '[' and i == ']':
                    stack.pop()
                elif stack[-1] == '{' and i == '}':
                    stack.pop()
                else:
                    stack.append(i)

            else:
                stack.append(i)

        if not stack:
            return Trues
        else:
            return False