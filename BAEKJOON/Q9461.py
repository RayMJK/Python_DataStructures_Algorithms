# DP

n = int(input())

dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(3, 101):
    dp[i] = dp[i-3] + dp[i-2]

print(dp[n-1])
