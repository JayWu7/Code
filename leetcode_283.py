# method 1
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        思路：  从0开始遍历nums里的值，不是0，i++； 是0，将当前值删掉，并在末尾加0，
        i不变，因为数组下标发生了变化，之前第i+1个元素的下标现在变为i，同时，因为0加在了后面，所以需要判断的值减1，length-1
        """
        i = 0
        length = len(nums)
        while i < length:
            if not nums[i]:  # num==0
                nums.pop(i)
                nums.append(0)
                length -= 1
            else:
                i += 1


# method 2   快慢指针
class Solution:
    def moveZeroes(self, nums):
        fast = slow = 0
        length = len(nums)
        while fast < length:
            if nums[fast]:  # 快指针不为0
                if not nums[slow]:  # 如果slow为0
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
