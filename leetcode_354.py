class Solution:
    def lengthOfLIS(self, nums):
        num_stack = []
        import bisect
        for num in nums:
            if not num_stack or num_stack[-1] < num:
                num_stack.append(num)
            else:
                num_stack[bisect.bisect_left(num_stack, num)] = num
        return len(num_stack)

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # 由宽度排序,如果宽度一样，按高度的逆序排
        return self.lengthOfLIS([envelope[1] for envelope in envelopes])


a = [[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]
s = Solution()
a = s.maxEnvelopes(a)
print(a)
