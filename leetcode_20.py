class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        思路： 遍历s，如果stack不为空，则把stack栈首元素和当前字母的对应括号比较，一致则弹出
        如果当前字母是另一种右边括号，则出错
        stack为空或者当前字母是左括号，则把当前字母加入栈中
        """
        dic = {')': '(', '}': '{', ']': '['}
        stack = []
        for l in s:
            if stack:
                if stack[-1] == dic.get(l):
                    stack.pop()
                    continue
                elif dic.get(l):
                    return False
            stack.append(l)
        return stack == []

s = Solution()
print(s.isValid('()'))
