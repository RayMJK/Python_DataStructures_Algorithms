def partitionLabels(S):
    """
    :type S: str
    :rtype: List[int]
    """
    d = {alphabet: index for index, alphabet in enumerate(S)}
    l = 0
    r = 0
    res = []
    for index, alphabet in enumerate(S):
        r = max(r, d[alphabet])
        if r == index:
            res.append(r - l + 1)
            l = index + 1

    return res

S= "ababcbacadefegdehijhklij"
print(partitionLabels(S))