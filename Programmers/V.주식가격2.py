def solution(prices):
    result = [0 for x in range(len(prices))]
    # print(result)
    for i in range(len(prices)):

        for j in range(i + 1, len(prices)):
            # print(i,j)
            if prices[i] <= prices[j]:
                result[i] += 1
            else:
                result[i] += 1
                break
    return result