import sys

def input_data() :
    readl = sys.stdin.readline
    N = int(readl())#협찬 물품의 수
    D = list(map(int, readl().split()))#선호도
    return N, D


def Solve():
    sol = -30001#첫번째 방법의 최대 선호도
    sum = 0
    for i in D :
        if sum > 0 :
            sum += i
        else :
            sum = i
        if sum > sol :
            sol = sum
    return sol

#입력받는 부분
N, D = input_data()
sol = Solve()
print(sol)#출력하는 부분
