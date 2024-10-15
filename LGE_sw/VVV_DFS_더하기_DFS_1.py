import sys

def Input_Data():
    N, K = map(int, readl().split())
    num = list(map(int, readl().split()))
    return N, K, num


def dfs_binary(n, remain): # n번 자연수 포함 여부 -> O, X
    if remain == 0:
        return True
    if remain < 0:
        return False
    if n >= N:
        return False

    if dfs_binary(n+1, remain-num[n]):
        return True
    if dfs_binary(n+1, remain):
        return True

    return False



sol = []
# 입력 받는 부분
readl = sys.stdin.readline

T = int(readl())
for _ in range(T):
    N, K, num = Input_Data()
    # 여기서부터 입력
    result = dfs_binary(0, K) # 이진 선택 (중복 순열)

    if result == True:
        sol.append("YES")
    else:
        sol.append("NO")




# 출력하는 부분
print(*sol, sep = '\n')