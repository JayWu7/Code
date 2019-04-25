class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        le,ri = 0,len(nums) - 1
        while le <= ri:
            mi = (le + ri) // 2
            if target == nums[mi]:
                return mi
            elif target < nums[mi] and (mi == 0 or target > nums[mi-1]):
                return mi
            elif target < nums[mi]:
                ri = mi
            else:
                le = mi + 1
        else:
            if ri == len(nums) - 1:
                return ri + 1