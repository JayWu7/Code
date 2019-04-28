# class Solution:
#     def nextGreaterElements(self, nums):
#         res = []
#         le = len(nums)
#         for i, n in enumerate(nums):
#             ind = i + 1
#             while ind != i:
#                 if ind == le:
#                     ind = 0
#                     continue
#
#                 if nums[ind] > n:
#                     res.append(nums[ind])
#                     break
#                 else:
#                     ind += 1
#             else:
#                 res.append(-1)
#
#         return res
# 暴力 超时


class Solution:
    def nextGreaterElements(self, nums):
        if not nums:
            return []
        stack = [0]
        res = [-1 for _ in nums]
        for i, n in enumerate(nums[1:], 1):
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n
            stack.append(i)


        for i in stack[1:]:
            for j in range(0,stack[0]+1):
                if nums[j] > nums[i]:
                    res[i] = nums[j]
                    break

        return res
