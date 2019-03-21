class Solution:
    def reverseVowels(self, s: str) -> str:
        # 双指针法
        left, right = 0, len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        sl = list(s)
        while left < right:
            if (sl[left] in vowels) ^ (sl[right] in vowels):
                if sl[left] in vowels:
                    right -= 1
                else:
                    left += 1
            else:
                if sl[left] in vowels:
                    sl[left], sl[right] = sl[right], sl[left]
                right -= 1
                left += 1
        return ''.join(sl)
