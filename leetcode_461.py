class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        def hammingWeight(n):
            x = 0
            while n:
                if n:
                    n = n & (n - 1)
                    x += 1
            return x
        and_x_y = x & y
        or_x_y = x | y
        return hammingWeight(or_x_y) - hammingWeight(and_x_y)

#method 2   直接异或操作
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        def hammingWeight(n):
            x = 0
            while n:
                if n:
                    n = n & (n - 1)
                    x += 1
            return x
        return hammingWeight(x ^ y)

#excellent code    思路： 每次比较n的最后一个二进制位是不是1，如果是，ans加1； 然后将n右移一位，直至n==0结束
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = x ^ y
        ans = 0
        while a > 0:
            if a & 1 == 1:
                ans += 1
            a >>= 1
        return ans