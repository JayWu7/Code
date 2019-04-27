class Solution:
    # time : 10 min
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s):
            stack = []
            for l in s:
                if l == '#':
                    if stack: stack.pop()
                else:
                    stack.append(l)
            return stack

        return helper(S) == helper(T)
