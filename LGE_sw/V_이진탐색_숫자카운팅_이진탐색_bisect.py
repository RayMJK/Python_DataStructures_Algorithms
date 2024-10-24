import sys
import bisect

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	num = [0] + list(map(int, readl().split()))
	M = int(readl())
	query = list(map(int, readl().split()))
	return N, num, M, query

def solve_bisect():
	for q in query:
		lower = bisect.bisect_left(num, q, lo=1)
		if lower != len(num) and num[lower] == q:
			upper = bisect.bisect_right(num, q, lo=1)
			sol.append(upper-lower)
		else:
			sol.append(0)
	return sol

sol = []
# 입력받는 부분
N, num, M, query = Input_Data()

# 여기서부터 작성
sol = solve_bisect()

# 출력하는 부분
print(*sol)