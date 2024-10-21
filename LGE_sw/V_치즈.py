import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_ch = [list(map(int, readl().split())) for _ in range(R)]
    return R, C, map_ch


def flood_fill(r,c):
    melt = 0
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    q = deque()

    map_ch[r][c] = 2
    q.append((r,c))

    while q:
        x,y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not 0<=nx<=R-1:
                continue
            if not 0<=ny<=C-1:
                continue
            if map_ch[nx][ny] == 0:
                q.append((nx,ny))
                map_ch[nx][ny] = 2
            elif map_ch[nx][ny] == 1:
                map_ch[nx][ny] = 3
                melt+=1
    return melt


def melt_cheese():
    for r in range(R):
        for c in range(C):
            if map_ch[r][c] == 3 or map_ch[r][c] == 2:
                map_ch[r][c] = 0

def solve():
    cnt_cheese = 0
    for row in map_ch:
        cnt_cheese += sum(row)

    hour = 0
    while cnt_cheese:
        last_ch = cnt_cheese
        melt = flood_fill(0,0)
        cnt_cheese -= melt
        melt_cheese()
        hour += 1

    return hour, last_ch

sol_hour, sol_last_cnt_ch = -1, -1
# 입력받는 부분
R, C, map_ch = Input_Data()

# 여기서부터 작성
sol_hour, sol_last_cnt_ch = solve()

# 출력하는 부분
print(sol_hour, sol_last_cnt_ch, sep='\n')