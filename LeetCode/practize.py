def solution(n, m):
    answer = []
    if max(n, m) % min(n, m) == 0:
        answer.append(min(n, m))
        answer.append(max(n, m))
        return answer
    else:

        for i in range(1, min(n, m) + 1):
            gcf = 1
            if min(n, m) % i == 0:
                if max(n, m) % i == 0:
                    if i > gcf:
                        gcf = i
    lcm = min(n, m) * max(n, m) / gcf
    answer.append(gcf)
    answer.append(lcm)
    return answer

print(solution(14,56))