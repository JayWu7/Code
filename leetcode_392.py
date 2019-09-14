class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        thinking: iterate the t, and find if all the letters of s are in t and also in the right sequence
        '''
        if not s:
            return True
        index, length = 0, len(s)
        for letter in t:
            if s[index] == letter:
                index += 1
                if index == length:
                    return True
        return False


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        using the built-in function find
        '''
        i = 0
        for letter in s:
            i = t.find(letter, i)
            if i == -1:
                return False
            i += 1
        return True