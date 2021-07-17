class Solution:
    def findTheDifference(self, s: str, t: str):
        if not s:
            return t

        dic = {}
        for l in t:
            if l in dic:
                dic[l] += 1
            else:
                dic[l] = 1

        for l in s:
            dic[l] -= 1

        for k, v in dic.items():
            if v:
                return k
