class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        a = set(nums)

        for i in a:
            if nums.count(i) > length / 2:
                return i