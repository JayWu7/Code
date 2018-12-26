#method1 212ms
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        思路： 先遍历一遍，看每一个字母出现的次数，然后返回第一个值为1的字母，没有则返回-1
        """
        s_dict = {}
        for l in s:
            if l in s_dict:
                s_dict[l] += 1
            else:
                s_dict[l] = 1
        for i, l in enumerate(s):
            if s_dict[l] == 1:
                return i
        return -1


# method2   116ms
class Solution:
    '''
    思路：  使用有序字典，模拟队列，遍历s，如果l不在queue中，且不在exist中，则在queue中添加键为l，值为i的元素
    返回queue第一个元素的值
    '''

    def firstUniqChar(self, s):
        from collections import OrderedDict
        queue = OrderedDict()
        exist = set()
        for i, l in enumerate(s):
            if l in queue:
                queue.pop(l)
                exist.add(l)
            elif l in exist:
                pass
            else:
                queue[l] = i
        if queue:
            return queue.popitem(last=False)[1]
        return -1


