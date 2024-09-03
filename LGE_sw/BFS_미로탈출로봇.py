import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    W, H = map(int, readl().split())
    sw, sh, ew, eh = map(int, readl().split())
    map_maze = [[0] + list(map(int, readl().strip())) + [0] if 1<=h<=H else [0] * (W+2) for h in range(H+2)]
    return W, H, sw, sh, ew, eh, map_maze


sol = -1
# 입력 받는 부분
W, H, sw, sh, ew, eh, map_maze = Input_Data()

# 여기서부터 작성
visited = [[False]*(W+2) for _ in range(H+2)]
directions = [(-1,0),(1,0),(0,1),(0,-1)]

def bfs():
    q=deque()
    q.append((sh, sw))

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 1 or nx > H or ny < 1 or ny > W:
                continue
            if visited[nx][ny] == True or map_maze[nx][ny] == 1:
                continue
            visited[nx][ny] = True
            map_maze[nx][ny] = map_maze[x][y] + 1
            q.append((nx,ny))
            if nx == eh and ny == ew:
                return map_maze[nx][ny]
    return -1

sol = bfs()

# 출력하는 부분
print(sol)