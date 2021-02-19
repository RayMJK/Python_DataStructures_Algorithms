def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    answer = []
    for h, k in sorted(people, key=lambda x: (-x[0], x[1])):

        answer.insert(k, [h, k])
        print(answer)
    return answer

print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
