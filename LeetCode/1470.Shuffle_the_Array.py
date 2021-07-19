def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    answer = []
    a = nums[:n]
    b = nums[n:]
    print(a)
    print(b)
    for i in range(n):
        answer.append(a[i])
        answer.append(b[i])
    return answer

print(shuffle([2,5,1,3,4,7], 3))
