import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [0] + list(map(int, readl().split()))
    T = int(readl())
    query = list(map(int, readl().split()))
    return N, num, T, query


def binary_search(s, e, d):
    while s<=e:
        m = (s+e)//2
        if num[m] == d:
            return m
        elif num[m] > d:
            e = m-1
        else:
            s = m+1
    return -1

def solve():
    sol = []
    for q in query:
        # Binary_Search(s, e, d)
        ret = binary_search(1, N, q)
        if ret == -1:
            sol.append(0)
        else:
            sol.append(ret)
    return sol

# 입력받는 부분
N, num, T, query = Input_Data()

# 여기서부터 작성
sol = solve()

# 출력하는 부분
print(*sol, sep='\n')
