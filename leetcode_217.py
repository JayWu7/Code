class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_nums = set(nums)
        if len(set_nums) == len(nums):
            return False
        return True


#metgod two
# class Solution:
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         return len(set(nums)) != len(nums)

#method Three
# class Solution:
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         set_nums = set()
#         for num in nums:
#             if num in set_nums:
#                 return True
#             set_nums.add(num)
#         return False