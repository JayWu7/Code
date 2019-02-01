class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        思路： 实际上就是十进制转二十六进制
        """
        letter_dict = {i: l for i, l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)}
        res = []
        while n:
            mod = n % 26
            n //= 26
            if mod == 0:
                n -= 1
                mod = 26
            res.append(letter_dict[mod])
        return ''.join(reversed(res))
