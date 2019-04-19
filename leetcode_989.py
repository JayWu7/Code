class Solution:
    def addToArrayForm(self, A: list[int], K: int) -> list[int]:
        x, b = 0, 1
        for a in A[::-1]:
            x += a * b
            b *= 10

        sum = str(x + K)
        res = []
        for s in sum:
            res.append(int(s))
        return res
