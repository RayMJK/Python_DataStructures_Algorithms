def solution(n, m):
    answer = []
    result = []
    for i in range(1, min(n,m)+1):
        if min(n,m)%i == 0:
            if max(n,m) % i == 0:
                answer.append(i)
    if len(answer) == 1:
        gcf = answer.pop()
        result.append(gcf)
        result.append(n*m)
    else:
        gcf = answer.pop()
        lcm = max(n,m)
        result.append(gcf)
        result.append(lcm)
    return result

print(solution(1000000, 999999))