import sys

sys.setrecursionlimit(100000)


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans_list = []
    visited = [[False] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and visited[i][j] == False:
                dfs(i, j, visited, n, m, maps)
    return answer


def dfs(x, y, visited, n, m, maps):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= m or ny < 0 or ny > n:
            continue
        if maps[nx][ny] == 1:
            dfs(nx, ny, visited, n, m, maps)


'''
[
    [1,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,0,1],
    [0,0,0,0,1]
]
'''