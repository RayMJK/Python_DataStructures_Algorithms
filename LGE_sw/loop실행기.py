import sys

def input_data():
    readl = sys.stdin.readline
    loop = readl().strip()
    return loop


# 재귀 함수
def solve(loop, s):
    p = s
    cnt = int(loop[s+1])
    while cnt:
        cnt -= 1
        p = s+2
        while loop[p] != '>':
            if loop[p] != '<':
                print(loop[p], end='')
            else : # loop[p] == '<'
                p = solve(loop, p)
            p+=1
    return p


# 입력 받는 부분
loop = input_data()

# 코드를 작성하세요
solve(loop, 0)
