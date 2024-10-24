import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_num = [int(readl()) for _ in range(N)]
    return N, list_num


# Case 1: 내장 함수를 이용
def Reverse(num):
    return int(''.join(reversed(str(num))))


'''
# Case 2: 산술 연산 이용
def Reverse(num):
    rev = 0
    while num:
        rev = rev * 10 + num % 10
        num //= 10
    return rev
'''


def Solve(list_num):
    l = []
    for num in list_num:
        sum = num + Reverse(num)
        l.append("YES" if sum == Reverse(sum) else "NO")
    return l


ans = []
# 입력 받는 부분
N, list_num = Input_Data()

# 여기서부터 작성
ans = Solve(list_num)

# 출력받는 부분
print(*ans, sep='\n')