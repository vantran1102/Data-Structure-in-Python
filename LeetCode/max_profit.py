#brute-force option:
# def max_profit(prices):
#     max= 0
#     for buy in range(len(prices)):
#         for sell in range(buy+1,len(prices)):
#             profit = prices[sell]-prices[buy]
#             if profit > max:
#                 max = profit
#     return max

def max_profit(prices):
    if len(prices) < 2:
        return 0
    min = prices[0]
    max = 0
    for current_price in prices[1:]:
        profit = current_price - min
        if profit > max:
            max = profit
        if current_price < min:
            min = current_price
    return max
prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


"""
    EXPECTED OUTPUT:
    ----------------
    Test with mixed prices:
    Prices: [7, 1, 5, 3, 6, 4]
    Maximum profit: 5
    -----------------------------
    Test with descending prices:
    Prices: [7, 6, 4, 3, 1]
    Maximum profit: 0
    -----------------------------
    Test with ascending prices:
    Prices: [1, 2, 3, 4, 5, 6]
    Maximum profit: 5
    -----------------------------

"""