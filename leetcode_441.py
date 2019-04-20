class Solution:
    def arrangeCoins(self, n: int) -> int:
        N = n * 2
        k = int((2 * n) ** 0.5)
        while k ** 2 + k > N:
            k -= 1
        return k



