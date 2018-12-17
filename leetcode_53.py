class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub = cur = nums[0]
        for num in nums[1:]:
            if cur > 0:
                cur = cur + num
            else:
                cur = num
            max_sub = cur if cur > max_sub else max_sub
        return max_sub
