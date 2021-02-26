class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def get_next_num(n):
            total_sum = 0
            while n > 0:
                n, num = n // 10, n % 10
                total_sum += num ** 2
            return total_sum

        result = set()

        while n != 1 and n not in result:
            result.add(n)
            n = get_next_num(n)

        return n == 1