def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    hash_table = {}

    for num in nums:
        hash_table[num] = 1

    answer = []

    for num in range(1, len(nums) + 1):
        if num not in hash_table:
            answer.append(num)

    return answer