class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin_nums = nums
        self.cur_nums = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        #self.cur_nums = self.origin_nums[:]
        #return self.cur_nums
        return self.origin_nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        from random import shuffle
        shuffle(self.cur_nums)
        return self.cur_nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()