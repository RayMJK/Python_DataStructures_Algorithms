import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int,readl().split())
    map_jewel = [[0] + list(readl()[:-1]) + [0] if 1<=r<=R else [0]*(C+2) for r in range(R+2)]
    return R, C, map_jewel

def bfs(r,c):
    q = deque()
    visited = [[False] * (C+2) for _ in range(R+2)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q.append((r,c,0))
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

def get_start():
    q_start = deque()
    [q_start.append((r,c)) for r in range(1, R+1) for c in range(1, C+1) if map_jewel[r][c] == 'L']
    return q_start

def solve(q_start):
    return max([bfs(r,c) for r,c in q_start])



sol = -1
# 입력받는 부분
R, C, map_jewel = Input_Data()

# 여기서부터 작성
q_start = get_start()
sol = solve(q_start)

# 출력하는 부분
print(sol)