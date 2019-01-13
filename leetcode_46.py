class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        思路： 分解为左部分和当前数字的排列
        """
        if not nums:
            return []

        def helper(left, num):
            res = []
            for n in left:
                for i in range(len(left) + 1):
                    cur = n[:i] + [num] + n[i:]
                    if cur not in res:
                        res.append()

            return res

        res = [[nums[0]]]
        for num in nums[1:]:
            res = helper(res, num)
        return res


#method 2  利用Python内置函数

class Solution:
    def permute(self, nums):
        from itertools import permutations
        return list(permutations(nums,len(nums)))

