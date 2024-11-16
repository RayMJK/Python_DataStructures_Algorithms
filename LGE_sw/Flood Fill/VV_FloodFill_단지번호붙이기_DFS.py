import sys


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_apt = [list(map(int,list(readl().strip()))) for r in range(N)]
	return N, map_apt


size = 0
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def flood_fill_dfs(r,c):
	global size
	map_apt[r][c] = 0
	size += 1

	for dr, dc in directions:
		nr, nc = r+dr, c+dc
		if not 0<=nr<=N-1:
			continue
		if not 0<=nc<=N-1:
			continue
		if map_apt[nr][nc] == 0:
			continue
		flood_fill_dfs(nr,nc)

def solve():
	global size
	list_size = []
	sys.setrecursionlimit(N*N)
	for r in range(N):
		for c in range(N):
			if map_apt[r][c] == 0:
				continue
			size = 0
			flood_fill_dfs(r,c)
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