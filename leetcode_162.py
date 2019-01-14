class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if not length:
            return
        if length == 1 or nums[1] < nums[0]:
            return 0
        if nums[-1] > nums[-2]:
            return length - 1
        index = 1
        while index < len(nums) - 1:
            if (nums[index - 1] < nums[index]) and nums[index + 1] < nums[index]:
                return index
            else:
                index += 1


#method2  使用二分
class Solution:
    def findPeakElement(self, nums):
        length = len(nums)
        if not length:
            return
        if length == 1 or nums[1] < nums[0]:
            return 0
        if nums[-1] > nums[-2]:
            return length - 1
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                return mid
            elif nums[mid - 1] > nums[mid]:
                right = mid
            else:
                left = mid + 1

