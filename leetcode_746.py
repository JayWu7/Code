class Solution:
    def minCostClimbingStairs(self, cost):

        n = len(cost)
        dp = [float('inf') for _ in range(n + 1)]

        dp[0], dp[1] = cost[0], min(cost[0], cost[1])

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]





