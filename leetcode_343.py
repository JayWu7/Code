# class Solution:
#     def integerBreak(self, n: int) -> int:
#         '''
#
#         change the n to as more as possible number three. left transfer to two
#         '''
#
#
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        if n == 4:
            return 4

        dp = [0 for _ in range(n + 1)]  # add one more number on the left for easy to understand
        dp[1], dp[2], dp[3], dp[4] = 1, 2, 3, 4

        for k in range(5, n + 1):
            dp[k] = max(dp[i] * dp[k - i] for i in range(1, k // 2 + 1))

        return dp[-1]

#剪绳子
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        if n == 4:
            return 4

        dp = [0 for _ in range(n + 1)]  # add one more number on the left for easy to understand
        dp[1], dp[2], dp[3], dp[4] = 1, 2, 3, 4

        for k in range(5, n + 1):
            dp[k] = max(dp[i] * dp[k - i] for i in range(1, k // 2 + 1))

        return dp[-1]


class Solution:
    def cuttingRope(self, n: int) -> int:
        max=0
        if n==2:
            return 1
        for i in range(2,n//2+2):
            max1=0
            if n%i==0:
                max1=(n//i)**i
            else:
                max1=(n//i+1)**(n%i)*(n//i)**(i-n%i)
            if max1>max:
                max=max1
        # print(max)
        return max%1000000007