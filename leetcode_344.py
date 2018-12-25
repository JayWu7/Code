class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


# method 2
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        注意 ：  str是静态对象，不能改变
        双指针，一前一后  遍历s，
        将s的右半部分加到left上，将左半部分加到right上
        然后返回  left + right
        """
        l, r = 0, len(s) - 1
        left = right = ''
        while l < r:
            left = left + s[r]
            right = s[l] + right
            l += 1
            r -= 1
        if l == r:
            left = left + s[l]
        return left + right


# method 3  思路和method2一样，不过先转为list处理
class Solution:
    def reverseString(self, s):
        l, r = 0, len(s) - 1
        list_s = list(s)
        while l < r:
            list_s[l], list_s[r] = list_s[r], list_s[l]
            l += 1
            r -= 1
        return ''.join(list_s)
