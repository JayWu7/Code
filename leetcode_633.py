class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 思路： a，b一定小于 c**1/2  ， 暴力
        a, b = 0, int(c ** 0.5) + 1
        while a <= b:
            r = a**2 + b**2
            if r == c:
                return True
            elif r < c:
                a += 1
            else:
                b -= 1
        else:
            return False


# Excellent code
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c <= 2:
            return True
        while c % 2 == 0:
            c = c // 2
        p = 3
        while p * p <= c:
            index = 0
            while c % p == 0:
                index += 1
                c = c // p
            if (p % 4 == 3) and (index % 2 == 1):
                return False
            p += 2
        return c % 4 == 1