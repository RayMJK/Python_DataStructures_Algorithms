import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [list(map(int, readl().split())) for _ in range(N)]
    return N, pos


def bfs(sr, sc):
    q = deque()
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    edge = 0

    map_list[sr][sc] = 2
    q.append((sr, sc))

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if not min_r <= nr <= max_r: continue
            if not min_c <= nc <= max_c: continue
            if map_list[nr][nc] == 0:
                map_list[nr][nc] = 2
                q.append((nr, nc))
            elif map_list[nr][nc] == 1:
                edge += 1
    return edge


sol = -1
# 입력받는 부분
N, pos = Input_Data()

# 여기서부터 작성
map_list = [[0] * 102 for _ in range(102)]
min_c = 100
max_c = 1
min_r = 100
max_r = 1
for position in pos:
    map_list[position[1]][position[0]] = 1
    if position[0] >= max_c:
        max_c = position[0]
    if position[0] <= min_c:
        min_c = position[0]
    if position[1] >= max_r:
        max_r = position[1]
    if position[1] <= min_r:
        min_r = position[1]

min_r -= 1
max_r += 1
min_c -= 1
max_c += 1
sol = bfs(min_r, min_c)

# 출력하는 부분
print(sol)
