import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [0] + list(map(int, readl().split()))
    M = int(readl())
    query = list(map(int, readl().split()))
    return N, num, M, query


def binary_search_lower(s, e, d):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if num[m] == d:
            sol = m
            e = m-1
        elif num[m] > d:
            e = m-1
        else:
            s = m+1
    return sol

def binary_search_upper(s, e, d):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if num[m] == d:
            sol = m
            s = m+1
        elif num[m] > d:
            e = m-1
        else:
            s = m+1
    return sol


def solve():
    sol = []
    for q in query:
        lower = binary_search_lower(1, N, q)
        if lower == -1:
            sol.append(0)
        else:
            upper = binary_search_upper(1, N, q)
            sol.append(upper-lower+1)
    return sol


# 입력받는 부분
N, num, M, query = Input_Data()

# 여기서부터 작성
sol = solve()

# 출력하는 부분
print(*sol)
