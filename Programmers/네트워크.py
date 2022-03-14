def solution(n, computers):
    answer = 0
    #print(computers)
    for i in range(len(computers)):
        print(i)
        for j in range(i, n):
            if j == i:
                continue
            if computers[i][j] == 1:
                answer += 1
    return n - answer
