# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        思路： 二分搜索，题目要找的是第一个错误的版本
                        即找到一个版本是错误版本，且它上一个版本不是错误版本
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):  # 是错误版本
                if mid == 1:  # 第一个版本
                    return 1
                elif isBadVersion(mid - 1) is False:
                    return mid
                else:
                    right = mid - 1
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    left = mid + 1


# excellent code    经典二分思想
class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
