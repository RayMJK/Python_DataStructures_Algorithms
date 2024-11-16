import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0]*(N+1) for n in range(N+1)]
	return N, matrix

def DFS(cnt, cur, sum_cost):
	global sol

	if sol <= sum_cost :
		return
	if cnt == N:
		if matrix[cur][1] and sol > sum_cost + matrix[cur][1] :
			sol = sum_cost + matrix[cur][1]
		return


	for n in range(2, N+1):
		if visited[n] == True:
			continue
		if matrix[cur][n] == 0:
			continue
		visited[n] = True
		DFS(cnt+1, n, sum_cost+matrix[cur][n])
		visited[n] = False

sol = -1
# 입력 받는 부분
N, matrix = Input_Data()

# 여기서부터 작성
sol = 9999999999
visited = [False] * (N+1)
DFS(1, 1, 0)

# 출력하는 부분
print(sol)