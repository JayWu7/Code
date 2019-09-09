class Solution:
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        count = 0
        for l in s[::-1]:
            if l == ' ':
                break
            count += 1

        return count