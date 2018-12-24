class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            longest, length = 0, 1
        else:
            return 0

        for i, n in enumerate(nums[1:]):  # 从1开始计数，刚好表示当前值的下一个元素的下标
            if n > nums[i]:
                length = length + 1
            else:
                longest, length = length if length > longest else longest, 1
        return longest if longest > length else length


s = Solution()
print(s.findLengthOfLCIS([1, 3, 5, 7]))
