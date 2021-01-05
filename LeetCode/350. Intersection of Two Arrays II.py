def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    a = sorted(nums1)  # [1,1,2,2]
    b = sorted(nums2)  # [2,2]
    i = 0
    result = []
    while i < len(a):
        j = 0
        while j < len(b):
            if a[i] == b[j]:
                c = a[i]
                b.pop(j)
                result.append(c)
            j += 1
        i += 1


    return result

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersect(nums1, nums2))


