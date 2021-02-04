def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    answer = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                answer.append(i)
                answer.append(j)

    return answer

nums = [3,3]
target = 6
print(twoSum(nums, target))