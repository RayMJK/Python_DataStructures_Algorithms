import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [list(map(int, readl().split())) for _ in range(N)]
    return N, pos

def make_map():
    min_r, min_c = 100, 100
    max_r, max_c = 0, 0
    map_field = [[0] * 102 for _ in range(102)]

    for c, r in pos:
        map_field[r][c] = 1
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)
    min_r -= 1
    max_r += 1
    min_c -= 1
    max_c += 1
    return min_r, max_r, min_c, max_c, map_field

def flood_fill_bfs(r,c):
    q = deque()
    q.append((r,c))
    map_field[r][c] = 2

    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    edge = 0

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not min_r<=nx<=max_r:
                continue
            if not min_c<=ny<=max_c:
                continue
            if map_field[nx][ny] == 0:
                map_field[nx][ny] = 2
                q.append((nx,ny))
            elif map_field[nx][ny] == 1:
                edge += 1
    return edge


sol = -1
# 입력받는 부분
N, pos = Input_Data()

# 여기서부터 작성
min_r, max_r, min_c, max_c, map_field = make_map()
sol = flood_fill_bfs(min_r, min_c)

# 출력하는 부분
print(sol)
