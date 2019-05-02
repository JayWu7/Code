class Solution:
    '''
    思路： 遍历数组，如果当前数是val，则将数组最后的元素和这个数交换
    time: 5min
    '''

    def removeElement(self, nums, val: int) -> int:
        length, i = len(nums), 0

        while i < length:
            if nums[i] == val:
                nums[i], nums[length - 1] = nums[length - 1], nums[i]
                length -= 1
            else:
                i += 1

        return length
