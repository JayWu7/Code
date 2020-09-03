# class Solution:
#     def new21Game(self, N: int, K: int, W: int) -> float:
#         points = [v for v in range(K, K + W)]  # possible final values
#         if N >= points[-1]:
#             return 1.0
#         if N < points[0]:
#             return 0.0
#
#         pw = 1 / W
#         dp = [0.0] + [pw for _ in range(W)] + [0.0 for _ in range(W + 1, N + 1)]
#         for p in range(W + 1, N + 1):
#             start = p - W if p - W > 0 else 1
#             dp[p] = sum([dp[k] for k in range(start, p)]) * pw
#
#         return sum(dp[K:])
#
# S = Solution()
# print(S.new21Game(21, 17, 10))


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        dp[K - 1] = float(min(N - K + 1, W)) / W
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]
