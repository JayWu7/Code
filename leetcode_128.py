class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        start, length, same = 0, 1, 0

        nums.sort()
        for i, num in enumerate(nums[1:]):
            if nums[i] == num - 1:
                continue
            elif nums[i] == num:
                same = same + 1
            else:
                l, start, same = i - start + 1 - same, i + 1, 0
                length = l if l > length else length
 
        return length if length > len(nums) - start else len(nums) - start


s = Solution()
print(s.longestConsecutive([0, -1, 1, 2]))

#excellent code  (O(n),利用set)
# class Solution:
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         longest_streak = 0
#         num_set = set(nums)
#
#         for num in num_set:
#             if num - 1 not in num_set:
#                 current_num = num
#                 current_streak = 1
#
#                 while current_num + 1 in num_set:
#                     current_num += 1
#                     current_streak += 1
#
#                 longest_streak = max(longest_streak, current_streak)
#
#         return longest_streak
