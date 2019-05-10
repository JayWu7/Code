class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        思路： dict 储存数字和对应下标
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                for ind in dic[n]:
                    if i - ind <= k:
                        return True
                dic[n].append(i)
            else:
                dic[n] = [i]
        else:
            return False


#faster way
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        思路： dict 储存数字和对应下标
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, n in enumerate(nums):
            if n in dic and i - dic[n] <= k:
                return True
            else:
                dic[n] = i
        else:
            return False

#more faster
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        思路： dict 储存数字和对应下标
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, n in enumerate(nums):
            if n in dic and i - dic[n] <= k:
                return True
            dic[n] = i
        return False

#using setdefault way
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        思路： dict 储存数字和对应下标
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, n in enumerate(nums):
            if 0 != i - dic.setdefault(n,i) <= k:
                return True
            dic[n] = i
        return False