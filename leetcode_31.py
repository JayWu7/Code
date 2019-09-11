class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.

        first, use a variable to represent the value of original num
        and also define a variable to store the possible upper num.

        """

        def helper(a, i):
            while i > 0:
                for j in range(i - 1, a - 1, - 1):
                    if nums[j] < nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                        nums[j + 1:] = reversed(nums[j + 1:])
                        return
                    elif nums[j] == nums[i]:
                        helper(j, i - 1)
                i -= 1
            nums.reverse()

        helper(0, len(nums) - 1)


# excellent code

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n > 1:
            q = 0
            for i in range(n - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    break
                else:
                    j = i
                    while j < n - 1 and nums[j] >= nums[j + 1]:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
                        j += 1
                    if j < n - 1:
                        q = 1
                        while j > i - 1:
                            nums[j], nums[j + 1] = nums[j + 1], nums[j]
                            j -= 1
                if q == 1:
                    break
