import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    A, B = map(int, readl().split())
    S = int(readl())
    seq = [int(readl()) for _ in range(S)]
    return N, A, B, S, seq
'''
s : 지금 처리해야 할 순서 번호
left, right : 열려있는 책장 번호
sum_move : 문 이동 누적 횟수
'''

def DFS(s, left, right, sum_move):
    global sol
    if sol <= sum_move:
        return
    if s >= S:
        sol = sum_move
        return

    if seq[s] < right:
        DFS(s + 1, seq[s], right, sum_move + abs(left - seq[s]))

    if left < seq[s]:
        DFS(s + 1, left, seq[s], sum_move + abs(right - seq[s]))


sol = -1

# 입력받는 부분
N, A, B, S, seq = Input_Data()

# 여기서부터 작성
sol = 9999999999999
DFS(0, min(A, B), max(A, B), 0)

# 출력하는 부분
print(sol)