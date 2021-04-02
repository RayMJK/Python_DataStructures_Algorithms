def solution(N, stages):
    answer = []
    result = {}
    stages.sort()
    stage = 1
    count = 0
    for i in range(1, N+1):
        if (len(stages)-count) == 0:
            result[i] = 0
            continue
        rate = stages.count(i) / (len(stages)-count)
        count += stages.count(i)
        result[i] = rate
    print(result)
    sequence = sorted(result.items(), key=lambda x: x[1], reverse = True)
    print(sequence)
    for i in sequence:
        answer.append(i[0])
    return answer


print(solution(5,[2, 1, 2, 4, 2, 4, 3, 3]))