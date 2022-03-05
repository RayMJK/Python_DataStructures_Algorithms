def solution(money):
    answer = 0
    # 첫 번째 집을 털었을때 = > 마지막집 털지 않음
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 첫번째 집 털지 않았을때 => 마지막집 까지.
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    answer = max(max(dp1), max(dp2))
    return answer