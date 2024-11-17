import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_jewel = [[0] + list(readl()[:-1]) + [0] if 1 <= r <= R else [0] * (C + 2) for r in range(R + 2)]
    return R, C, map_jewel


def bfs(r, c):
    q = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * (C + 2) for _ in range(R + 2)]
    q.append((r, c, 0))
    visited[r][c] = True

    while q:
        x, y, distance = q.popleft()
        for dx, dy in directions:
            nx, ny, n_time = x + dx, y + dy, distance + 1
            if not 1 <= nx <= R:
                continue
            if not 1 <= ny <= C:
                continue
            if map_jewel[nx][ny] != "L":
                continue
            if visited[nx][ny] == True:
                continue
            q.append((nx, ny, n_time))
            visited[nx][ny] = True

    return distance


def solve():
    result = []
    for i in list_a:
        length = bfs(i[0], i[1])
        result.append(length)
    return max(result)


sol = -1
# 입력받는 부분
R, C, map_jewel = Input_Data()

# 여기서부터 작성
list_a = []
for r in range(1, R + 1):
    for c in range(1, C + 1):
        if map_jewel[r][c] == 'L':
            list_a.append((r, c))

sol = solve()

# 출력하는 부분
print(sol)
