def solution(maps):
    answer = 0
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    ans_list = []
    visited = [[False] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and visited[i][j] == False:
                dfs(i,j)
    return answer


'''
[
    [1,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,0,1],
    [0,0,0,0,1]
]
'''