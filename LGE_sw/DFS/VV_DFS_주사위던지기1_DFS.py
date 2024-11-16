import sys

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    return N, M


def Dice1(n):
    # n번째 주사위 던졌을때 나올 숫자 선택 (중복순열)
    if n >= N:
        print(*dice)
        return

    for i in range(1, 6+1):
        # n번째 주사위 숫자 -> i
        dice[n] = i
        Dice1(n+1)

def Dice2(n, s):
    # 중복 조합
    if n >= N:
        print(*dice)
        return

    for i in range(s, 6+1):
        dice[n] = i
        Dice2(n+1, i)
        # Dice2(n+1, i+1) -> 그냥 조합 일때.

def Dice3(n):
    # 순열
    if n >= N:
        print(*dice)
        return

    for i in range(1, 6+1):
        if sel[i] == True:
            continue
        dice[n] = i
        sel[i] = True
        Dice3(n+1)
        sel[i] = False

def solve():
    # 주사위 던지기 순서번호 : 0 ~ N-1# 주사위 던지기 순서번호 : 0 ~ N-1
    if M == 1:
        Dice1(0)
    elif M == 2: # n: 주사위 던지기 순서번호, s : 선택 시작 숫자
        Dice2(0, 1)
    elif M == 3: # n : 주사위 던지기 순서번호
        Dice3(0)

# 입력 받는 부분
N, M = Input_Data()

# 여기서부터 작성
dice = [0] * N # dice[n] : n번째 던진 주사위의 숫자
sel = [False] * 7 # sel[n] : n숫자의 현재 진행중인 경우의 수에서 선택 여부 (순열 경우의 수 시도에서 사용)
solve()

