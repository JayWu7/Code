# method 1  循环
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        思路： 循环计算3的幂次方，并和n比较
        """
        x = 0
        while True:
            cur = 3 ** x
            if cur > n:
                return False
            if cur == n:
                return True
            x += 1

import math
#excellent code
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        maxint = 0x7fffffff

        k = math.log(maxint) // math.log(3)
        b3 = 3 ** k
        return (b3 % n) == 0