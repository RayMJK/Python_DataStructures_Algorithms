def solution(N, stages):
    answer = []
    stages.sort()
    stage = 1
    count = 0
    for i in range(1, N+1):
        rate = stages.count(i) / (len(stages)-count)
        count += stages.count(i)
        answer.append(rate)
    return answer