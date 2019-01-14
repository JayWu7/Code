# method 1
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        from collections import defaultdict

        res = defaultdict(list)

        for num in nums:
            res[num].append(num)

        nums[:] = res[0] + res[1] + res[2]


# method2
class Solution:
    def sortColors(self, nums):
        '''思路：三指针
        第一个指针代表0的位置，第二个指针代表2的位置，第三个指针一直走
        '''
        first = third = 0
        second = len(nums) - 1
        while third <= second:
            if nums[third] == 0:
                nums[third], nums[first] = nums[first], nums[third]
                first += 1

            elif nums[third] == 2:
                nums[third], nums[second] = nums[second], nums[third]
                second -= 1
                third -= 1  # 从末尾换一个数过来，需要再处理一遍这个数，因为之前没有遍历到这个数，所以不确定是否为1
            third += 1
