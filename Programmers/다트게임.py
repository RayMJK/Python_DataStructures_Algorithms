def solution(dartResult):
    answer = 0

    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            answer += int(dartResult[:i]) ** 1
        elif dartResult[i] == 'D':
            answer += int(dartResult[:i]) ** 2
        elif dartResult[i] == 'T':
            answer += int(dartResult[:i]) ** 3

        dartResult = dartResult[i+1:]


    return answer

print(solution('1S2D3T'))