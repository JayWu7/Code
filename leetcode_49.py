class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_list = []
        res = []
        for str in strs:
            cur = list(str)
            cur.sort()
            if cur in str_list:
                res[str_list.index(cur)].append(str)
            else:
                str_list.append(cur)
                res.append([str])
        return res


#method 2  使用defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        str_dict = defaultdict(list)
        for str in strs:
            str_dict[tuple(sorted(str))].append(str)
        return str_dict.values()

#method3  使用内置字典
class Solution(object):
    def groupAnagrams(self, strs):
        str_dic = {}
        for str in strs:
            cur = tuple(sorted(str))
            if cur in str_dic:
                str_dic[cur].append(str)
            else:
                str_dic[cur] = [str]
        return str_dic.values()