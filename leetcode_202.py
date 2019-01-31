class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        used = set()
        while n != 1:
            used.add(n)
            str_n, n = str(n), 0
            for l in str_n:
                n += int(l) ** 2
            if n in used:
                return False
        return True
