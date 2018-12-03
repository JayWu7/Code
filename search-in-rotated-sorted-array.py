class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except ValueError:
            return -1

#Excellent code  (二分查找)
# class Solution:
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if not nums:
#             return -1
#         low,high = 0,len(nums)-1
#         while low <= high:
#             mid = (low + high) // 2
#             if nums[mid] == target:
#                 return mid
#             if nums[low] <= nums[mid]:
#                 if nums[low]<= target<= nums[mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             else:
#                 if nums[mid]<= target <=nums[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#         return -1
