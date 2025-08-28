# Function to find the maximum profit
def maxProfitRec(price, start, end):
    res = 0

    # Consider every valid pair, find the profit with it
    # and recursively find profits on left and right of it
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            if price[j] > price[i]:
                curr = (price[j] - price[i]) + \
                       maxProfitRec(price, start, i - 1) + \
                       maxProfitRec(price, j + 1, end)
                res = max(res, curr)
    return res

# Wrapper function
def maximumProfit(prices):
    return maxProfitRec(prices, 0, len(prices) - 1)

if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(maximumProfit(prices)) #output : 865