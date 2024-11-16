import sys
import bisect


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [0] + list(map(int, readl().split()))
    T = int(readl())
    query = list(map(int, readl().split()))
    return N, num, T, query


def solve_bisect():
    sol = []
    for q in query:
        ret = bisect.bisect_left(num, q, lo=1, hi=len(num))
        if ret != len(num) and num[ret] == q:
            sol.append(ret)
        else:
            sol.append(0)
    return sol

# 입력받는 부분
N, num, T, query = Input_Data()

# 여기서부터 작성
sol = solve_bisect()


# 출력하는 부분
print(*sol, sep='\n')
