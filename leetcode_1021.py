class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = ''
        start = 0
        for i, s in enumerate(S):
            if s == '(':
                stack.append(s)
            else:
                stack.pop()
                if not stack:
                    res += S[start + 1:i]
                    start = i + 1
        return res
