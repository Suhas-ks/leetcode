class Solution:
    # try to get a gradient, if value is greater than previous value, then sell else buy; if it continuously increases without a drop, decide between
    # lowest and highest point
    def maxProfit(self, prices):
        profit = 0
        num_days = len(prices)
        trans_count = 0
        for i in range(1, num_days):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
                trans_count += 1
            else:
                continue
        if trans_count == num_days - 1:
            return prices[num_days - 1] - prices[0]
        return profit


# sol = Solution()
# print(sol.maxProfit([1, 2, 3, 4, 5]))
# print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
# print(sol.maxProfit([7, 6, 4, 3, 1]))
# print(sol.maxProfit([6, 1, 3, 2, 4, 7]))
