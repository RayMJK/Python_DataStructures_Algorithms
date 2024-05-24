import sys

def input_data() :
	readl = sys.stdin.readline
	N = int(readl())#협찬 물품의 수
	D = list(map(int, readl().split()))#선호도 
	return N, D


// 다이나믹 프로그래밍 (카데인 알고리즘)
def Solve():
	for i in range(1, len(D)) :
		D[i] = max(D[i], D[i] + D[i-1])
	return max(D)

#입력받는 부분
N, D = input_data()
sol = Solve()
print(sol)#출력하는 부분
