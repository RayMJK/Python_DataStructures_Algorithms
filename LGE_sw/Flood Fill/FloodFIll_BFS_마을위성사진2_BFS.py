import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_lake = [[0] + list(map(int,list(readl().strip()))) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N, map_lake


def bfs(r,c):
    q = deque()
    q.append((r,c))
    directions = [(-1,0), (1,0), (0,-1), (0,1), (1,1), (-1,1), (1,-1), (-1,-1)]
    map_lake[r][c] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not 1<=nx<=N:
                continue
            if not 1<=ny<=N:
                continue
            if map_lake[nx][ny] == 0:
                continue
            q.append((nx,ny))
            map_lake[nx][ny] = 0


def solve():
    cnt = 0
    for r in range(1, N+1):
        for c in range(1, N+1):
            if map_lake[r][c] == 0:
                continue
            bfs(r,c)
            cnt += 1
    return cnt



sol = -1
# 입력 받는 부분
N, map_lake = Input_Data()

# 여기서부터 작성
sol = solve()

# 출력하는 부분
print(sol)

'''
[
[0, 0, 0, 0, 0, 0, 0], 
[0, 0, 1, 0, 1, 0, 0], 
[0, 1, 0, 0, 0, 1, 0], 
[0, 0, 1, 0, 1, 0, 0], 
[0, 0, 0, 1, 0, 0, 0], 
[0, 1, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0]
]
'''