class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_dict = {l: i for i, l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)}
        res, length = 0, len(s)
        for l in s:
            length -= 1
            res = res + 26 ** length * letter_dict[l]
        return res
