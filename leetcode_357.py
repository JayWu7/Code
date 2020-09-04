class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        k = 10
        if n == 1:
            return k
        if n > 10:
            n = 10
        for i in range(2, n+1):
            s = i-1
            m = 9
            n = 9
            while s > 0:
                m *= n
                n -= 1
                s -= 1
            k += m
        return k 