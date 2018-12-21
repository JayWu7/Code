# 解法一，普通解法
# class Solution:
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         pre = nums[0]  #前一个num
#         for num in nums[1:]:
#             if num == pre:
#                 nums.remove(num)
#             else:
#                 pre = num
#         return len(nums)

# 解法二，利用Python set不包含重复元素的特性

class Solution:
    def removeDuplicates(self, nums):
        set_nums = set(nums)
        nums[:] = sorted(list(set_nums))
        return len(nums)


# 解法三，双指针法

class Solution:
    def removeDuplicates(self, nums):
        length = len(nums)
        if length <= 1:
            return length
        index = 0
        for i in range(length - 1):
            if nums[i] != nums[i + 1]:
                nums[index + 1] = nums[i + 1]
                index += 1
        return index + 1
