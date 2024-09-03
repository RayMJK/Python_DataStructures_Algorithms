import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_uv = [[0] + list(map(int, readl().strip())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
	return N, map_uv

'''
print(map_uv)
[
	[0, 0, 0, 0, 0], 
	[0, 0, 4, 1, 0], 
	[0, 2, 5, 3, 0], 
	[0, 6, 2, 0, 0], 
	[0, 0, 0, 0, 0]
]
'''
sol = -1
# 입력 받는 부분
N, map_uv = Input_Data()

# 여기서부터 작성
directions = [(-1,0), (1,0), (0,-1), (0,1)]
chk = [[999]*(N+2) for _ in range(N+2)]
chk[1][1] = map_uv[1][1]
def bfs():
	q = deque()
	q.append((1,1))
	while q:
		x, y = q.popleft()
		for dx, dy in directions:
			nx, ny = x+dx, y+dy
			# if nx < 1 or nx > N or ny < 1 or ny > N:
			# 	continue

			if not 1 <= nx <= N :
				continue
			if not 1 <= ny <= N :
				continue
			if chk[nx][ny] <= chk[x][y] + map_uv[nx][ny]:
				continue
			chk[nx][ny] = chk[x][y] + map_uv[nx][ny]
			q.append((nx,ny))

	return chk[N][N]

sol = bfs()
# 출력하는 부분
print(sol)