class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = len(nums)
        num_majority = num / 2

        a = sorted(nums)
        b = set(nums)

        result = {}
        for i in b:
            result[i] = a.count(i)

        answer = [k for k, v in result.items() if max(result.values()) == v]

        the_answer = answer.pop()

        return the_answer
