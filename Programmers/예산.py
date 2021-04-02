def solution(d, budget):
    answer = 0
    d.sort()
    if budget < d[0]:
        return 0
    for i in d:
        if budget >= i:
            budget -= i
            answer += 1
        else:
            break

    return answer

