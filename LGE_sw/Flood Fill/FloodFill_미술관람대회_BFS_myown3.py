import copy
import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_nor_pig = [[0] + list(readl()[:-1]) + [0] if 1 <= r <= N else [0] * (N + 2) for r in range(N + 2)]
    return N, map_nor_pig


def bfs(map_art, x, y):
    q = deque()
    q.append((x,y))
    color = map_art[x][y]

    map_art[x][y] = 0

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not 1<=nx<=N:
                continue
            if not 1<=ny<=N:
                continue
            if map_art[nx][ny] != color:
                continue
            q.append((nx,ny))
            map_art[nx][ny] = 0

def solve(map_art):
    cnt = 0
    for r in range(1, N+1):
        for c in range(1, N+1):
            if map_art[r][c] == 0:
                continue
            bfs(map_art,r,c)
            cnt += 1
    return cnt


sol_nor_pig, sol_rg_pig = -1, -1
# 입력받는 부분
N, map_nor_pig = Input_Data()

# 여기서부터 작성
map_rg_pig = copy.deepcopy(map_nor_pig)
for r in range(1, N+1):
    for c in range(1, N+1):
        if map_rg_pig[r][c] == 'R':
            map_rg_pig[r][c] = 'G'


sol_nor_pig = solve(map_nor_pig)
sol_rg_pig = solve(map_rg_pig)

# 출력하는 부분
print(sol_nor_pig, sol_rg_pig)