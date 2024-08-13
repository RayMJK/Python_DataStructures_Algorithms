import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    visited[x][y] = True
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >=n or ny < 0 or ny >= m:
            continue
        if array[nx][ny] == 1 and visited[nx][ny] == False:
            dfs(nx, ny)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    array = [[0] * m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int,input().split())
        array[x][y] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1 and visited[i][j] == False:
                dfs(i,j)
                result += 1
    print(result)
'''
array = 
[
 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
 [0, 0, 1, 1, 0, 0, 0, 1, 1, 1], 
 [0, 0, 0, 0, 1, 0, 0, 1, 1, 1], 
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 ]

visited = \
[
     [False, False, False, False, False, False, False, False, False, False], 
     [False, False, False, False, False, False, False, False, False, False], 
     [False, False, False, False, False, False, False, False, False, False], 
     [False, False, False, False, False, False, False, False, False, False], 
     [False, False, False, False, False, False, False, False, False, False], 
     [False, False, False, False, False, False, False, False, False, False], 
     [False, False, False, False, False, False, False, False, False, False], 
     [False, False, False, False, False, False, False, False, False, False]
]
'''

