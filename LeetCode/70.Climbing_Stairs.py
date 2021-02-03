def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    dp = {1: 1, 2: 2, 3: 3}

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(climbStairs(6))