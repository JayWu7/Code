#merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2

        left_part = self.sortArray(nums[:mid])  # left part
        right_part = self.sortArray(nums[mid:])

        # merge them
        i = j = k = 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                nums[k] = left_part[i]
                i += 1
            else:
                nums[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            nums[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            nums[k] = right_part[j]
            j += 1
            k += 1

        return nums
