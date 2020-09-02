class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(m,n):0}
        for s in strs:
            num0 = s.count('0')
            num1 = s.count('1')
            for (n0,n1),value in dp.copy().items():
                if n0>=num0 and n1>=num1:
                    dp[(n0-num0,n1-num1)] = max(dp.get((n0-num0,n1-num1),0),value+1)
        return max(dp.values())