class Solution(object):
    def wordPattern(self, pattern, str):
        """
        #思路： 使用dict
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        have = set()
        str = str.split(' ')
        if len(str) != len(pattern): return False
        for p, s in zip(pattern, str):
            if p in dic:
                if dic[p] != s:
                    return False
            elif s in have:
                return False
            else:
                dic[p] = s
                have.add(s)
        return True


#use dic.values, much faster
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        #思路： 使用dict
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        str = str.split(' ')
        if len(str) != len(pattern): return False
        for p, s in zip(pattern, str):
            if p in dic:
                if dic[p] != s:
                    return False
            elif s in dic.values():
                return False
            else:
                dic[p] = s
        return True

