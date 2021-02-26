def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0

    profit = 0

    buy_stock = prices[0]

    for i in range(len(prices)):
        if prices[i] < buy_stock:
            buy_stock = prices[i]

        profit = max((prices[i]-buy_stock, profit))

    return profit

prices = [1,6,4,3,1]
print(maxProfit(prices))