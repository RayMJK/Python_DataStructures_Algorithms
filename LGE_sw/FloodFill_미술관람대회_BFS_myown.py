import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_nor_pig = [[0] + list(readl()[:-1]) + [0] if 1 <= r <= N else [0] * (N + 2) for r in range(N + 2)]
    return N, map_nor_pig


def bfs(r, c):
    q = deque()
    q.append((r, c))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    global visited
    visited[r][c] = True

    while q:
        x, y = q.popleft()
        color = map_nor_pig[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not 1 <= nx <= N:
                continue
            if not 1 <= ny <= N:
                continue
            if map_nor_pig[nx][ny] != color:
                continue
            if visited[nx][ny] == True:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True

def bfs_rg(r, c):
    q2 = deque()
    q2.append((r, c))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    global visited_rg
    visited_rg[r][c] = True

    while q2:
        x, y = q2.popleft()
        color = map_nor_pig[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not 1 <= nx <= N:
                continue
            if not 1 <= ny <= N:
                continue
            if map_nor_pig[nx][ny] != color:
                continue
            if visited_rg[nx][ny] == True:
                continue
            q2.append((nx, ny))
            visited_rg[nx][ny] = True



def solve():
    cnt = 0
    global visited
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if visited[r][c] == True:
                continue
            bfs(r, c)
            cnt += 1

    return cnt

def solve_rg():
    cnt_rg = 0
    global visited_rg
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if map_nor_pig2[r][c] == "G":
                map_nor_pig2[r][c] = "R"

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if visited_rg[r][c] == True:
                continue
            bfs_rg(r, c)
            cnt_rg += 1

    return cnt_rg

# 입력받는 부분
N, map_nor_pig = Input_Data()
map_nor_pig2 = map_nor_pig

# 여기서부터 작성
visited = [[False] * (N + 2) for _ in range(N + 2)]
visited_rg = [[False] * (N + 2) for _ in range(N + 2)]
sol_nor_pig = solve()
sol_rg_pig = solve_rg()
# 출력하는 부분
print(sol_nor_pig, sol_rg_pig)

'''
[
	[0, 0, 0, 0, 0, 0, 0], 
	[0, 'R', 'R', 'R', 'B', 'B', 0], 
	[0, 'G', 'G', 'B', 'B', 'B', 0], 
	[0, 'B', 'B', 'B', 'R', 'R', 0], 
	[0, 'B', 'B', 'R', 'R', 'R', 0], 
	[0, 'R', 'R', 'R', 'R', 'R', 0],
	[0, 0, 0, 0, 0, 0, 0]
 ]
'''
