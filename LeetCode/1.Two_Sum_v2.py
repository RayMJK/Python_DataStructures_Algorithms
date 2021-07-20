def twoSum(nums, target):
    hm = {}
    for i in range(len(nums)):
        hm[nums[i]] = i

    print(hm)
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hm and hm[complement] != i:
            return [i, hm[complement]]


print(twoSum([2,7,11,15], 9))
