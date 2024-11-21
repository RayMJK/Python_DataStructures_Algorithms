import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    needs = list(map(int, readl().split()))
    M = int(readl())
    return N, needs, M

def check(limit):
	s = 0
	for n in needs:
		if n < limit:
			s += n
		else:
			s += limit
	if s <= M:
		return True
	else:
		return False

def solve():
	s = 0
	e = max(needs)
	while s<=e:
		m = (s+e)//2
		if check(m):
			sol = m
			s = m+1
		else:
			e = m-1
	return sol

sol = -1
# 입력받는 부분
N, needs, M = Input_Data()

# 여기서부터 작성
sol = solve()
# 출력하는 부분
print(sol)