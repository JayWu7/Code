class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        if l1 > l2:
            le = l1
            num2 = '0'* (l1-l2) + num2
        elif l2 > l1:
            le = l2
            num1 = '0'*(l2 - l1) + num1
        else:
            le = l1
        res, ad = '', 0
        for i in range(-1, -le - 1, -1):  # iterate from left to right
            t = int(num1[i]) + int(num2[i]) + ad
            ad = 0
            if t >= 10:
                ad = 1
                t -= 10

            res = str(t) + res
        if ad == 0:
            return res
        else:
            return '1' + res
