def solution(money):
    answer = 0
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    # print(dp1, dp2)

    # 1번집을 터는 경우 => 마지막 집 제외
    # 2번 부터 마지막 바로 전 집까지.
    dp1[0] = money[0]
    for i in range(1, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 1번 집을 안 터는 경우 => 2번부터 마지막집까지.
    dp2[0] = 0
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    answer = max(dp1[-2], dp2[-1])
    return answer