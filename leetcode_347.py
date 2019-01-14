class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_num = {}
        for num in nums:
            if num in dict_num:
                dict_num[num] += 1
            else:
                dict_num[num] = 1

        from heapq import nlargest
        k_largest = nlargest(k, dict_num, key=lambda k: dict_num[k])
        return k_largest


#method 2   使用Counter
class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        res = Counter(nums)
        return [n[0] for n in res.most_common(k)]
