import sys
import bisect
def Input_Data():
    readl = sys.stdin.readline
    M, N, L = map(int, readl().split())
    shoots = list(map(int, readl().split()))
    animals = [list(map(int, readl().split())) for _ in range(N)]
    return M, N, L, shoots, animals


def solve():
    shoots.sort()
    cnt = 0
    for x,y in animals:
        if y > L:
            continue
        low = x-(L-y)
        up = x+(L-y)

        idx = bisect.bisect_left(shoots, low)
        if idx != M and shoots[idx] <= up:
            cnt += 1
    return cnt


# 입력받는 부분
M, N, L, shoots, animals = Input_Data()

# 여기서부터 작성
sol = solve()

# 출력받는 부분
print(sol)