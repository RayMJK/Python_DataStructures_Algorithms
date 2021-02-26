class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        result = [0, k, k * k]

        for i in range(3, n + 1):
            result.append((result[i - 1] + result[i - 2]) * (k - 1))

        return result[n]