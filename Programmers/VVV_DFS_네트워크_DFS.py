def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i, visited)
            answer += 1
    return answer

def dfs(n, computers, num, visited):
    visited[num] = True
    for i in range(n):
        if i != num and computers[num][i] == 1:
            if visited[i] == False:
                dfs(n, computers, i, visited)

