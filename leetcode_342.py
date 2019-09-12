class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        cur = 1
        while cur <= num:
            if cur == num:
                return True
            cur <<= 2  # using the bit operation
        else:
            return False


