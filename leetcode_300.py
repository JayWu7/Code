class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_stack = []
        import bisect
        for num in nums:
            if not num_stack or num_stack[-1] < num:
                num_stack.append(num)
            else:
                num_stack[bisect.bisect_left(num_stack, num)] = num
        return len(num_stack)
