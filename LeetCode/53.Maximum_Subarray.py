def maxSubArray(nums): # Greedy
    """
    :type nums: List[int]
    :rtype: int
    """

    curr_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))