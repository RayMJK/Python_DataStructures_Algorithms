import sys
import bisect

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = [int(readl()) for _ in range(N)]
	return N, pos

def solve():
	pos.sort()
	cnt = 0
	for s1 in range(N-2):
		for s2 in range(s1+1, N-1):
			jump = pos[s2] - pos[s1]
			rs = pos[s2] + jump
			re = pos[s2] + 2*jump
			lower = bisect.bisect_left(pos, rs)
			if lower != N and pos[lower] <= re:
				upper = bisect.bisect_right(pos, re)
				cnt += upper-lower
	return cnt


sol = -1
# 입력받는 부분
N, pos = Input_Data()

# 여기서부터 작성
sol = solve()

# 출력하는 부분
print(sol)