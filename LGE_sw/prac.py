import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	matrix = [[0] + list(map(int, readl().split())) if 1<=s<=N else [0] * (N+1) for s in range(0, N+1)]
	return N, M, matrix


def bfs():
	q = deque()
	chk = [999999999] * (N+1)
	prev = [0] * (N+1)


	q.append((1,0))
	chk[1] = 0

	while q:
		n, time = q.popleft()
		if chk[n] < time:
			continue

		for nn in range(1, N+1):
			n_time = time + matrix[n][nn]
			if chk[nn] <= n_time:
				continue
			q.append((nn, n_time))
			chk[nn] = n_time
			prev[nn] = n
	return chk[M], prev

def get_route():
	route = []
	n = M
	while n != 0:
		route.append(n)
		n = prev[n]
	route.reverse()
	return route

sol = -1
route = []
# 입력 받는 부분
N, M, matrix = Input_Data()

# 여기서부터 작성
sol, prev = bfs()
route = get_route()

# 출력하는 부분

print(sol)
print(*route)