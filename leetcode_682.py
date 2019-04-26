class Solution:
    def calPoints(self, ops):
        '''
        思路: 利用栈储存历史记录
        时间：40min
        '''
        stack = []
        for p in ops:
            if p == '+':
                point = stack[-1] + stack[-2]
            elif p == 'D':
                point = stack[-1] * 2
            elif p == 'C':  # p==C
                stack.pop()
                continue
            else:
                point = int(p)
            stack.append(point)
        return sum(stack)


s = Solution()
s.calPoints(["36", "28", "70", "65", "C", "+", "33", "-46", "84", "C"])
