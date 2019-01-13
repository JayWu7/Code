class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        思路： 一个数组的子集，等于此数组，加上减去任一个数后数组的子集
        """
        sub = []

        def helper(nums):
            if nums in sub:
                return
            sub.append(nums)
            for i in range(len(nums)):
                helper(nums[:i] + nums[i + 1:])

        helper(nums)
        return sub


#method2
class Solution:
    def subsets(self, nums):
        '''
        思路：遍历nums，当前子集等于之前数字的子集和当前数的集合
        '''
        sub = [[]]
        for num in nums:
            sub.extend([[num] + left_sub for left_sub in sub])
        return sub


# Excellent code
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            for temp in res[:]:
                x = temp[:]
                x.append(num)
                res.append(x)
        return res
