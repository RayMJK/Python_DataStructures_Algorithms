import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    M, N = map(int, readl().split())
    map_box = [[0] + list(map(int, readl().split())) + [0] if 1<=r<=N else [0] * (M+2) for r in range(N+2)]
    return M, N, map_box


sol = -1
# 입력 받는 부분
M, N, map_box = Input_Data()
'''
print(map_box)
[
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
]
'''
# 여기서부터 작성
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs():
    q = deque()
    cnt_tomato = 0

    for r in range(1, N+1):
        for c in range(1, M+1):
            if map_box[r][c] == 1:
                q.append((r,c,0))
            elif map_box[r][c] == 0:
                cnt_tomato += 1
    if cnt_tomato == 0 :
        return 0

    while q:
        x, y, time = q.popleft()
        for dx, dy in directions:
            nx, ny, n_time = x+dx, y+dy, time+1
            if not 1<= nx <= N:
                continue
            if not 1<= ny <= M:
                continue
            if map_box[nx][ny] != 0 :
                continue
            map_box[nx][ny] = 1
            q.append((nx, ny, n_time))
            cnt_tomato -= 1
            if cnt_tomato == 0 :
                return n_time

    return -1

sol = bfs()

# 출력하는 부분
print(sol)