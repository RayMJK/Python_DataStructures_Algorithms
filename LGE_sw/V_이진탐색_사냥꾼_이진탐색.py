import sys

def Input_Data():
    readl = sys.stdin.readline
    M, N, L = map(int, readl().split())
    shoots = list(map(int, readl().split()))
    animals = [list(map(int, readl().split())) for _ in range(N)]
    return M, N, L, shoots, animals

def bs_low(list_data, s, e, d):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if list_data[m] >= d:
            sol = m
            e = m-1
        else:
            s = m+1
    return sol

def solve():
    shoots.sort()
    cnt = 0
    for x,y in animals:
        if y > L:
            continue
        low = x-(L-y)
        up = x+(L-y)
        idx_lower = bs_low(shoots, 0, M-1, low)
        if idx_lower < 0 or shoots[idx_lower] > up:
            continue
        cnt += 1
    return cnt


sol = -1

# 입력받는 부분
M, N, L, shoots, animals = Input_Data()

# 여기서부터 작성
sol = solve()


# 출력받는 부분
print(sol)