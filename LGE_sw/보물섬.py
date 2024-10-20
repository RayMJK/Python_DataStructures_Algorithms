import sys


def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_jewel = [[0] + list(readl()[:-1]) + [0] if 1 <= r <= R else [0] * (C + 2) for r in range(R + 2)]
    return R, C, map_jewel


sol = -1
# 입력받는 부분
R, C, map_jewel = Input_Data()

# 여기서부터 작성


# 출력하는 부분
print(sol)