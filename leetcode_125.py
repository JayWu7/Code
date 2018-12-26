class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        思路： 双指针，一左一右
        """
        lower_s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if lower_s[left] == lower_s[right]:
                left += 1
                right -= 1
            else:
                if not lower_s[left].isalnum():
                    left += 1
                elif not lower_s[right].isalnum():
                    right -= 1
                else:
                    return False
        return True


s = Solution()
s.isPalindrome('0P')