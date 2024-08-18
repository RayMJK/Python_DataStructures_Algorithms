from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            bfs(n, computers, i, visited)
            answer += 1
    return answer

def bfs(n, computers, num, visited):
    visited[num] = True
    q = deque()
    q.append(num)
    while q:
        v = q.popleft()
        for i in range(n):
            if computers[v][i] == 1 and i != v:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True

