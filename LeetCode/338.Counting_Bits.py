class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(1, num + 1):
            result.append(result[i >> 1] + int(i & 1))

        return result