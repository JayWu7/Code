class Solution:
    def removeDuplicates(self, nums):
        '''
        Thinking: using double pointers traversing the array, a point to the current num, another point tp the insert
        position. When the current num has appeared more than two times, continue move the first pointer but stop the
        second pointer until the current num change to other elements. Repeat this step

        time:
        '''
        le = len(nums)
        if le < 3:
            return le
        cur = 2
        for i in range(2, le):
            if nums[i] != nums[cur - 2]:  # this num has appeared more than twice
                nums[cur] = nums[i]
                cur += 1

        return cur
