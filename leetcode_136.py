class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums) - 2, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]

#method 2
'''使用Python ^ 操作符
'''
class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result = result ^ num   #两个一样的数异或操作为0，一个数和0异或操作为自己
        return result

#method 3
class Solution:
    def singleNumber(self, nums):
        return sum(set(nums)) * 2 - sum(nums)