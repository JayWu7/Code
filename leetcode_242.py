class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        elif set(s) != set(t):
            return False
        else:
            return sorted(s) == sorted(t)

#method 2   (巨慢)
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        思路： 遍历s，如果l在t中，则在t中删除这个元素，一直到最后，看t是否为空
        """
        if len(s) != len(t):
            return False
        else:
            list_t = list(t)
            for l in s:
                if l in list_t:
                    list_t.remove(l)
                else:
                    return False
        return list_t == []

#method 3  (quick)

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        set_s = set(s)
        for l in set_s:
            if s.count(l) != t.count(l):
                return False
        return True
