class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # left_part = nums[-k:]
        # right_part = nums[:-k]
        nums[:] = nums[-k:] + nums[:-k]