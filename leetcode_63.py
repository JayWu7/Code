class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)]] + obstacleGrid
        dp = [[0] + row for row in dp]

        dp[0][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if dp[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m][n]
