# method 1
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        思路： 从s的最大子串依次到最小子串，看当前子串是否是回文串，是就返回当前子串
        """

        if not s:
            return ''

        length = len(s)

        for length_child in range(length, 0, -1):
            for i in range(length - length_child + 1):
                cur_child = s[i:length_child + i]
                if cur_child == cur_child[::-1]:
                    return cur_child


# method 2   动态规划
class Solution(object):
    def longestPalindrome(self, s):
        '''思路：先将长度为1，2的子串，判断是否为回文字符串，如果是，加入集合中
        之后的子串判断是否为回文串即可借助之前已经储存过的回文串
        '''
        length = len(s)
        if length == 0:
            return ''
        if length == 1:
            return s
        palindromes = [{''}]
        palindromes.append({l for l in s})  # 单个字符
        palindromes.append({s[i:i + 2] for i in range(length - 1) if s[i] == s[i + 1]})  # 双字符

        for n in range(3, length + 1):  # n = 当前子串的长度
            palindromes.append(set())
            if not palindromes[-3]:   #如果中间子串没有回文串，则当前长度子串一定没有回文串
                continue
            for i in range(length - n + 1):
                cur_child = s[i:i + n]
                mid = cur_child[1:-1]
                if mid in palindromes[-3] and cur_child[0] == cur_child[-1]:  # 中间子串是回文串
                    palindromes[-1].add(cur_child)
        while length > 0:
            if palindromes[length]:
                return palindromes[length].pop()
            length -= 1
s = Solution()
s.longestPalindrome("babad")

#excellent code
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) < 2 or s == s[::-1]:
            return s
        n = len(s)
        start, maxlen = 0, 1

        for i in range(1, n):

            odd = s[i - maxlen - 1:i + 1]
            even = s[i - maxlen:i + 1]

            if i - maxlen - 1 >= 0 and odd == odd[::-1]:
                start = i - maxlen - 1
                maxlen += 2
                continue
            if i - maxlen >= 0 and even == even[::-1]:
                start = i - maxlen
                maxlen += 1

        return s[start:start + maxlen]
