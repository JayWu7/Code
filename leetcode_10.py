class Solution:
    def isMatch(self, s, p):
        import re
        pattern = re.compile(p)
        if pattern.match(s) == None:
            return False
        else:
            return True 
