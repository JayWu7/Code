class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bn = bin(n)
        return bn.count('1')


#excellent code
#思路：  按位与运算 n与n-1 结果会使n的二进制中的1比原始少一个
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        while n:
            if n:
                n = n & (n-1)
                x += 1
        return x