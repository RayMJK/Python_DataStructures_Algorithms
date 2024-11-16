import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_uv = [[0] + list(map(int, readl().strip())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
	return N, map_uv

def bfs():
	q = deque()
	directions = [(-1,0), (1,0), (0,-1), (0,1)]
	chk = [[99999999] * (N+2) for _ in range(N+2)]

	q.append((1,1,map_uv[1][1]))
	chk[1][1] = map_uv[1][1]


	while q:
		x, y, sum_uv = q.popleft()
		if sum_uv > chk[x][y]:
			continue

		for dx, dy in directions:
			nx, ny = x+dx, y+dy,
			if not 1 <= nx <= N:
				continue
			if not 1 <= ny <= N:
				continue
			n_sum_uv = sum_uv + map_uv[nx][ny]
			if n_sum_uv >= chk[nx][ny]:
				continue
			q.append((nx,ny, n_sum_uv))
			chk[nx][ny] = n_sum_uv
	return chk[N][N]


sol = -1
# 입력 받는 부분
N, map_uv = Input_Data()

# 여기서부터 작성
sol = bfs()
# 출력하는 부분
print(sol)