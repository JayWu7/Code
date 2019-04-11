# class Solution:   超时
#     def find132pattern(self, nums) :
#         le = len(nums)
#
#         for i in range(le - 2):
#             for j in range(i+1,le-1):
#                 if nums[j] > nums[i]:
#                     for k in range(j+1,le):
#                         if nums[i] < nums[k] < nums[j]:
#                             return True
#
#         return False

#
# class Solution:  超时
#     # 三指针做法:
#     def find132pattern(self, nums):
#         i, le = 0, len(nums)
#         j = 1
#         while j < le - 1:
#             if nums[j] <= nums[i]:
#                 i = j  # 确保 i 取遍历过的数的最小值
#             else:
#                 k = j + 1
#                 while k < le:
#                     if nums[k] <= nums[i]:
#                         pass
#                     elif nums[k] >= nums[j]:
#                         j = k  # 确保 j 取遍历过的数的最大值
#                     else:
#                         return True
#                     k += 1
#             j += 1
#         return False


class Solution:
    def find132pattern(self, nums):

        stack = []
        _MIN = float('-inf')

        for num in nums[::-1]:  #倒叙遍历
            if num < _MIN:
                return True
            while stack and num > stack[-1]:
                _MIN = stack.pop()
            stack.append(num)

        return False

