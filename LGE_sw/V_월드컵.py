import sys


def Input_Data():
    readl = sys.stdin.readline
    n = map(int, readl().split())
    result = [[next(n) for w in range(3)] for t in range(6)]
    return result


def dfs(n, result):
    if n >= 15:
        return 1

    t1, t2 = match_info[n]

    for i in range(3):
        if result[t1][i] and result[t2][2 - i]:
            result[t1][i] -= 1
            result[t2][2-i] -= 1
            if dfs(n + 1, result):
                return 1
            result[t1][i] += 1
            result[t2][2-i] += 1
    return 0


def make_match_info():
    match_info = []
    for t1 in range(0, 5):
        for t2 in range(t1+1, 6):
            match_info.append((t1, t2))
    return match_info


def simple_check():
    bool_result = True
    for r in result:
        if sum(r) != 5:
            return False
    return bool_result
    # return all([sum(r) == 5 for r in result])


sol_list = []

match_info = make_match_info()

for _ in range(4):
    # 입력받는 부분
    result = Input_Data()
    sol_list.append(dfs(0, result) if simple_check() else 0)
# 여기서부터 작성

print(*sol_list)
