def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == 0:
            zero = nums.pop(i)
            nums.append(zero)
            n -= 1

        else:
            i += 1
    return nums

input = [0,0,1]
print(moveZeroes(input))