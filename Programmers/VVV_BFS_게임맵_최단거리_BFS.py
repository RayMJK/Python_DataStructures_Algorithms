from collections import deque

def solution(maps):
    answer = 0
    directions = [(-1,0), (1,0), (0,-1),(0,1)]
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        while q:
            x, y = q.popleft()
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == 1 and visited[nx][ny] == False:
                    maps[nx][ny] = maps[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx,ny))

        return maps[n-1][m-1]
    answer = bfs(0,0)
    if answer == 1:
        answer = -1
    return answer

