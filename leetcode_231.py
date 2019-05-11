class Solution(object):
    def isPowerOfTwo(self, n):
        """
        思路： 使用位运算
        time: 5min
        :type n: int
        :rtype: bool
        """
        start = 1
        while start <= n:
            if start == n:
                return True
            start = start << 1   #向右进一位
        return False

