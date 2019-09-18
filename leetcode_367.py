class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i, j = 1, num // 2 + 1
        while i <= j:
            mid = (i + j) // 2
            cur = mid ** 2
            if cur < num:
                i = mid + 1
            elif cur > num:
                j = mid
            else:
                return True

        return False
