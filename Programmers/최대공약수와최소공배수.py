def solution(n, m):
    answer = []
    if max(n, m) % min(n, m) == 0:
        answer.append(min(n, m))
        answer.append(max(n, m))
        return answer

    for i in range(1, min(n, m) + 1):
        if min(n, m) % i == 0:
            if max(n, m) % i == 0:
                gcf = i
    lcm = min(n, m) * max(n, m) // gcf
    answer.append(gcf)
    answer.append(lcm)
    return answer

print(solution(21, 24))