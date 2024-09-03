from collections import deque

import sys


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    R, C, S, K = map(int, readl().split())
    return N, M, R, C, S, K


sol = -1
# 입력 받는 부분
N, M, R, C, S, K = Input_Data()

# 여기서부터 작성
directions = [(2,1), (2,-1), (1,2), (1,-2), (-2,1), (-2,-1), (-1,2), (-1,-2)]
visited = [[False]*(M+2) for _ in range(N+2)]
def bfs():
    q = deque()
    q.append((R,C, 0))

    while q:
        x, y, time = q.popleft()
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny, ntime = x+dx, y+dy, time+1
            if nx < 1  or nx > N or ny < 1 or ny > M:
                continue
            if visited[nx][ny] == True :
                continue
            if nx == S and ny == K:
                return ntime
            visited[nx][ny] = True
            q.append((nx,ny,ntime))
    return -1

sol = bfs()
# 출력하는 부분
print(sol)