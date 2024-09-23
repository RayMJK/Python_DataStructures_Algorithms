import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    R, C, S, K = map(int, readl().split())
    return N, M, R, C, S, K

def bfs():
    visited = [[False] * (M+2) for _ in range(N+2)]
    directions = [(-2,1), (-2,-1), (-1,2), (-1,-2), (2,1), (2,-1), (1,2), (1,-2)]
    q = deque()
    q.append((R,C,0))
    visited[R][C] = True

    while q:
        x, y, time = q.popleft()
        for dx, dy in directions:
            nx, ny, n_time = x+dx, y+dy, time+1
            if not 1<=nx<=N:
                continue
            if not 1<=ny<=M:
                continue
            if visited[nx][ny] == True:
                continue
            if nx == S and ny == K:
                return n_time
            q.append((nx,ny,n_time))
            visited[nx][ny] = True
    return -1

sol = -1
# 입력 받는 부분
N, M, R, C, S, K = Input_Data()

# 여기서부터 작성
sol = bfs()

# 출력하는 부분
print(sol)