class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0

        dp = [-float('inf') for _ in nums]

        dp[0] = nums[0]

        for i, n in enumerate(nums[1:], 1):
            dp[i] = max(dp[i - 1] + n, n)

        return max(dp)