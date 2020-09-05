# class Solution:
#     def maxProfit(self, prices, fee):
#         dp = [0 for _ in range(len(prices))]
#         for i, price in enumerate(prices[1:], 1):
#             if price < prices[i - 1]:
#                 dp[i] = dp[i - 1]
#             else:
#                 dp[i] = max(dp[i - 1], max(dp[j - 1] + price - prices[j] for j in range(i)) - fee)
#
#         return dp[-1]
# 超时

class Solution(object):
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash


S = Solution()
print(S.maxProfit([1, 3, 2, 8, 4, 9], 2))
