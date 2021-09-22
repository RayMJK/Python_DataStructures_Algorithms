class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ['(', ')', '{', '}', '[', ']']
        b = {')': '(', '}': '{', ']': '['}
        stack = []
        # print(s)

        for i in s:
            if i not in b:
                stack.append(i)
            else:
                if len(stack) != 0:
                    c = stack.pop()
                    if c == b[i]:
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
