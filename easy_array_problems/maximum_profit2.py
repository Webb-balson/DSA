# Python program to find the max profit when
# multiple transactions are allowed

def maximum_profit(prices):
    res = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            res += prices[i] - prices[i-1]

    return res

if __name__ == "__main__":
    prices = [100,180,260,310,40,535,695]
    res = maximum_profit(prices)
    print(f"The maximum profit earned: {res}")