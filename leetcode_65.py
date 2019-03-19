class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            complex(s)
            #float(s)
        except:
            return False
        return True
