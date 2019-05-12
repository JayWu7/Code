# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pass


class Solution(object):
    def guessNumber(self, n):
        """
        #思路： 二分
        time: 5min
        :return:
        """
        le, ri = 1, n + 1
        while le <= ri:
            mi = (le + ri) // 2
            gus = guess(mi)
            if gus == 0:
                return mi
            elif gus == 1:
                le = mi + 1
            else:
                ri = mi


# change the tell sequence
class Solution(object):
    def guessNumber(self, n):
        """
        #思路： 二分
        time: 5min
        :return:
        """
        le, ri = 1, n + 1
        while le <= ri:
            mi = (le + ri) // 2
            gus = guess(mi)
            if gus == 1:
                le = mi + 1
            elif gus == -1:
                ri = mi
            else:
                return mi
