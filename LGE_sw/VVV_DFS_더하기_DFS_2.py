import sys

def Input_Data():
    N, K = map(int, readl().split())
    num = list(map(int, readl().split()))
    return N, K, num

def dfs_multi(s, remain):

    if remain == 0:
        return True
    if remain < 0 :
        return False
    for n in range(s, N):
        if dfs_multi(n+1, remain-num[n]):
            return True
    return False

sol = []
# 입력 받는 부분
readl = sys.stdin.readline

T = int(readl())
for _ in range(T):
    N, K, num = Input_Data()
    # 여기서부터 입력
    result = dfs_multi(0, K) # 조합

    if result == True:
        sol.append("YES")
    else:
        sol.append("NO")


# 출력하는 부분
print(*sol, sep = '\n')