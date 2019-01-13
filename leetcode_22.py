class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        思路： 回溯法，且只当当前括号有效才继续添加
        """
        res = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return res
