class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i, num in enumerate(nums):
            if i != num:
                return i
        return i + 1


# method 2   算出如果不缺少数字时总数的大小，然后减去nums的总数，就是缺失的那个数值
class Solution(object):
    def missingNumber(self, nums):
        right_sum = (len(nums) + 1) * len(nums) / 2
        return right_sum - sum(nums)
