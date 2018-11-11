class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        pattern = re.compile(p)
        if pattern.match(s) == None:
            return False
        else:
            return True
