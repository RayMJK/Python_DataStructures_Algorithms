def solution(n, computers):
    a = 0
    #print(computers)
    for i in range(len(computers)):
        print(i)
        for j in range(i, n):
            if j == i:
                continue
            if computers[i][j] == 1:
                a += 1
    print(a)
    answer = n-a
    return answer
