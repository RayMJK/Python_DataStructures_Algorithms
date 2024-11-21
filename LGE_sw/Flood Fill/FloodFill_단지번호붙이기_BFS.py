import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_apt = [list(map(int,list(readl().strip()))) for r in range(N)]
	return N, map_apt

def flood_fill_bfs(r,c):
	q = deque()
	directions = [(-1,0), (1,0), (0,-1), (0,1)]

	q.append((r,c))
	map_apt[r][c] = 0
	size = 1

	while q:
		r, c = q.popleft()
		for dr, dc in directions:
			nr, nc = r+dr, c+dc
			if not 0<=nr<=N-1:
				continue
			if not 0<=nc<=N-1:
				continue
			if map_apt[nr][nc] == 0:
				continue
			q.append((nr,nc))
			map_apt[nr][nc] = 0
			size += 1
	return size

def solve():
	list_size = []
	for r in range(N):
		for c in range(N):
			if map_apt[r][c] == 0 :
				continue
			size = flood_fill_bfs(r,c)
			list_size.append(size)

	list_size.sort()
	return list_size

cnt = -1
list_size = []

# 입력 받는 부분
N, map_apt = Input_Data()

# 여기서부터 작성
list_size = solve()
cnt = len(list_size)

# 출력하는 부분
print(cnt)
print(*list_size,sep='\n')