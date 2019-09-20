class Solution:
    def integerBreak(self, n: int) -> int:
        '''

        change the n to as more as possible number three. left transfer to two
        '''

        if n == 3 or n == 2:
            return n - 1

        res = 1
        while n > 4:
            n -= 3
            res *= 3
        return res * n
