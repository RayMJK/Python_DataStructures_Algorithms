import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    W, H = map(int, readl().split())
    sw, sh, ew, eh = map(int, readl().split())
    map_maze = [[0] + list(map(int, readl().strip())) + [0] if 1 <= h <= H else [0] * (W + 2) for h in range(H + 2)]
    return W, H, sw, sh, ew, eh, map_maze


def bfs():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * (W+2) for _ in range(H+2)] # chk[h][w] : h,w 상태에 대한 경험 유무 (True : 경험)
    q = deque()

    # 초기 상태 정의
    q.append((sh, sw, 0)) # (h,w,time)
    visited[sh][sw] = True

    while q:
        h, w, time = q.popleft()
        for dh, dw in directions:
            nh, nw, ntime = h+dh, w+dw, time + 1
            if not 1<= nh <= H:
                continue
            if not 1<= nw <= W:
                continue
            if map_maze[nh][nw] == 1 :
                continue
            if visited[nh][nw] == True :
                continue

            if nh == eh and nw == ew :
                return ntime
            q.append((nh, nw, ntime))
            visited[nh][nw] = True
    return -1


sol = -1
# 입력 받는 부분
W, H, sw, sh, ew, eh, map_maze = Input_Data()

# 여기서부터 작성
sol = bfs()

# 출력하는 부분
print(sol)
