# method 1   使用内置index
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        try:
            res = haystack.index(needle)
        except ValueError:
            res = -1
        return res


# method2    使用str.find函数
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        return haystack.find(needle)


# method3   使用暴力穷举
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        思路：  双指针同时遍历haystack和needle，如果haystack[i]==needle[j],则i,j都++
        否则，i退回 i-j+1 , j退回0
        """
        if not needle:
            return 0
        i = j = 0
        max_j = len(needle) - 1
        while i < len(haystack):
            if haystack[i] == needle[j]:
                if j == max_j:  # 匹配成功
                    return i - j
                else:
                    i += 1
                    j += 1
            else:
                i = i - j + 1
                j = 0
        return -1


# method3  kmp算法
#参考： https://blog.csdn.net/v_july_v/article/details/7041827
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        def find_next(cur):  # 计算next数组
            nex = [-1]  # 初始值为-1
            max_j = len(cur) - 1
            j, k = 0, -1
            while j < max_j:
                if k == -1 or cur[k] == cur[j]:
                    j += 1
                    k += 1
                    nex.append(k)
                else:
                    k = nex[k]
            return nex

        if not needle:
            return 0
        nex = find_next(needle)
        i = j = 0
        max_j = len(needle) - 1
        while i < len(haystack):
            if haystack[i] == needle[j] or j == -1:
                if j == max_j:  # 匹配成功
                    return i - j
                else:
                    i += 1
                    j += 1
            else:
                j = nex[j]
        return -1
