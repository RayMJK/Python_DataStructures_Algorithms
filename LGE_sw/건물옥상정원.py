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
ans = []
ans_list = []

# H = [5, 2, 4, 2, 6, 1]

# 코드를 작성 하세요
for i in range(N):
    if len(ans_list) == 0 :
        ans_list.append(H[i])
        ans.append(0)
    else:
        if ans_list[-1] > H[i] :
            ans.append(len(ans_list))
            ans_list.append(H[i])
        else :
            while len(ans_list) > 0:
                if ans_list[-1] <= H[i] :
                    ans_list.pop()
                else :
                    break
            ans.append(len(ans_list))
            ans_list.append(H[i])

# 출력
print(sum(ans))

