class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = []

        def backtrack(first = 0) :
            # if all intergers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]

                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        backtrack()
        return output