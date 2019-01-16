class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        思路：
        组合问题， 机器人一共要往右跳 m-1 步，往下跳 n-1 步, 一共跳 m+n-2 步
        """

        def helper(n):  # 求阶乘
            res = 1
            for i in range(2, n + 1):
                res *= i
            return res

        return helper(m + n - 2) // (helper(m - 1) * helper(n - 1))
        #return int(helper(m + n - 2) / (helper(m - 1) * helper(n - 1)))
