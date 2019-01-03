# #method 1   有问题
# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         思路： 先偷最大的，然后再剩余可偷的房屋里再偷最大的，直至没有房屋可偷
#         """
#         rooms = {key: (value, True) for key, value in enumerate(nums)}
#         rob_seq = sorted(zip(rooms.values(), rooms.keys()), reverse=True)
#         money = 0
#         for i in range(len(nums)):
#             if rooms[rob_seq[i][1]]:  # 是否可偷
#                 money += rob_seq[i][0][0]
#                 rooms[rob_seq[i][1]] = False
#                 rooms[rob_seq[i][1] + 1] = False
#                 rooms[rob_seq[i][1] - 1] = False
#         return money


# method 2   思路正确，结果正确，但是超时
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路： 有n个房屋能偷的最大金额，等于n-1个房屋序列能偷的最大金额，和n-2个房屋序列能偷的最大金额加上第n个屋子能偷的钱 的最大值
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob(nums[:-1]), self.rob(nums[:-2]) + nums[-1])


# method 3   斐波那契数列思想
class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        sum0 = nums[0]
        sum1 = nums[1] if nums[1] > nums[0] else nums[0]
        for i in range(2, len(nums)):
            sum = sum1 if sum1 > sum0 + nums[i] else sum0 + nums[i]
            sum0 = sum1
            sum1 = sum
        return sum1


# method 4   斐波那契数列思想  优化   (速度不如第3种方法)
class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        sum0 = nums[0]
        sum1 = nums[1] if nums[1] > nums[0] else nums[0]
        for i in range(2, len(nums)):
            sum0,sum1 = sum1,max(sum1,sum0+nums[i])
            #sum0, sum1 = sum1, sum1 if sum1 > sum0 + nums[i] else sum0 + nums[i]
        return sum1


s = Solution()
s.rob([1, 2, 3, 1])
