class Solution:
    def maxProfit(self, prices):
        profit = 0
        trans = 1
        price = 0
        for i in range(len(prices)):
            if i == 0:
                price = prices[0]
                continue
            if price > prices[i] and trans == 1:
                trans = -1
                price = prices[i]
            elif