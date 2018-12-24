class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        str_x = str(x)

        index_l = 0
        index_r = len(str_x) - 1

        while index_l <= index_r:
            if str_x[index_l] != str_x[index_r]:
                return False
            index_l += 1
            index_r -= 1

        return True
