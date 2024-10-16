import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    matrix = [[0] + list(map(int, readl().split())) if 1 <= n <= N else [0] * (N + 1) for n in range(N + 1)]
    return N, matrix

"""
matrix[a][b] : a번 건물을 b번땅에 짓는 비용
"""

def dfs(n, sum_cost):
    global sol
    if sol <= sum_cost:
        return
    if n > N:
        sol = sum_cost
        return

    for i in range(1, N+1):
        if visited[i] == True:
            continue
        visited[i] = True
        dfs(n+1, sum_cost + matrix[n][i])
        visited[i] = False

def solve():
    global sol
    sol = 100 * N
    dfs(1, 0)
    return sol


sol = -1
# 입력 받는 부분
N, matrix = Input_Data()

# 여기서부터 작성

visited = [False] * (N+1)
sol = solve()

# 출력하는 부분
print(sol)
