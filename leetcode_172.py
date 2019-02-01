class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        思路： 笨办法
        """
        total = 1
        for i in range(2, n + 1):
            total *= i
        str_sum = str(total)
        index = len(str_sum) - 1
        while index > 0:
            if str_sum[index] != '0':
                break
            index -= 1
        return len(str_sum) - index - 1

        # 超时 明日优化


class Solution:
    def trailingZeroes(self, n):
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
