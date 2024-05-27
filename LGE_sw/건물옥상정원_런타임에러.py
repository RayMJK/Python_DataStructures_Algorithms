import sys

def InputData():
    readl = sys.stdin.readline
    N = int(readl())
    H = [ int(readl()) for i in range(N) ]
    return N, H


# 입력
# N: 건물 수
# H: 건물 높이
N, H = InputData()
ans = 0

# 코드를 작성 하세요
# N = 6
# H = [5, 2, 4, 2, 6, 1]
#      0  1  2  3  4  5
for i in range(N-1):
    tmp = 0
    for j in range(i+1, N):
        if H[i] > H[j] :
            diff = H[i] - H[j]
            #print("i, j, diff = ", i, j, diff)
            tmp += 1
        else :
            break
    ans += tmp

# 출력
print(ans)

