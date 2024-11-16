import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_nor_pig = [[0] + list(readl()[:-1]) + [0] if 1 <= r <= N else [0] * (N + 2) for r in range(N + 2)]
    return N, map_nor_pig

def flood_fill(map_art, r, c):
    q = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q.append((r,c))
    color = map_art[r][c]
    map_art[r][c] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not 1 <= nx <= N:
                continue
            if not 1 <= ny <= N:
                continue
            if map_art[nx][ny] != color:
                continue
            q.append((nx,ny))
            map_art[nx][ny] = 0

def get_answer(map_art):
    cnt_area = 0
    for r in range(1,N+1):
        for c in range(1,N+1):
            if map_art[r][c] == 0:
                continue
            flood_fill(map_art, r, c)
            cnt_area += 1
    return cnt_area

def solve():
    return get_answer(map_nor_pig), get_answer(map_rg_pig)

# 입력받는 부분
N, map_nor_pig = Input_Data()

# 여기서부터 작성
map_rg_pig = [['R' if map_nor_pig[r][c] == 'G' else map_nor_pig[r][c] for c in range(N+2)] for r in range(N+2)]
sol_nor_pig, sol_rg_pig = solve()

# 출력하는 부분
print(sol_nor_pig, sol_rg_pig)