class Solution:
    def massage(self, nums: List[int]) -> int:

        if not nums:
            return 0
        dp = [0 for _ in range(len(nums) + 1)]
        dp[1] = nums[0]

        for i in range(1, len(nums)):
            dp[i+1] = max( [dp[j] for j in range(i)] ) + nums[i]
        
        return max(dp)

