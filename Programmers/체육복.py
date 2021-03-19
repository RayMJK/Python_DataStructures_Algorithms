def solution(n, lost, reserve):
    answer = 0
    num_of_lost = len(lost)
    cap = n - num_of_lost
    if len(reserve) == 0:
        return cap
    if num_of_lost == 0:
        return n

    for i in lost:
        if i in reserve:
            cap += 1
            reserve.remove(i)
            pass
        elif i - 1 in reserve:
            reserve.remove(i - 1)
            cap += 1
            pass
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            cap += 1
            pass

    answer += cap

    return answer

n = 7
lost = [1, 2, 3, 4, 5, 6, 7]
reserve = [1, 2, 3]

print(solution(n, lost, reserve))