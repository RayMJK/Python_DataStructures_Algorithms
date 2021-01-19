def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in nums:
        if nums.count(i) == 1:
            return i

nums = [4,1,2,1,2]
print(singleNumber(nums))