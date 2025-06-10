def maximize_profit(prices):
    max = prices[0]
    min = prices[0]
    for i in prices:
        if i > max:
            max = i
        else:
            if i < min:
                min = i
    return "(" + str(min) + "," + str(max) + ")"

print(maximize_profit([100,180,260,310,40,535,695]))
print(maximize_profit([36,74,17,90,13,38,19,100,89]))


