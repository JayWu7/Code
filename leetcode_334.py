# # method 1  暴力法 极慢
# class Solution(object):
#     def increasingTriplet(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         思路： 遍历数组，判断当前数字后续数字中是否有两个比当前数字大,记录比当前数字大的数
#         如果有，则在比当前数字大的数组组成的数组中，判断是否有递增的两个数
#         一直遍历到倒数第三个数字
#         """
#         length = len(nums)
#         if length < 3:
#             return False
#         bigger_nums = []
#         for i, num in enumerate(nums[:-2]):
#             for j in range(i + 1, length):
#                 if nums[j] > num:
#                     bigger_nums.append(nums[j])
#             total = len(bigger_nums)
#             if total > 1:  # >=2
#                 for k, big in enumerate(bigger_nums):
#                     for l in range(k + 1, total):
#                         if bigger_nums[l] > big:
#                             return True
#             bigger_nums.clear()  # clear() Python3 才有
#         return False


# method 2
class Solution(object):
    def increasingTriplet(self, nums):
        '''
            第一次遍历确定初值
            思路：贪心算法，从左到右一次遍历，记录最小值和次小值，并用贪心替换
        '''
        if len(nums) < 3:
            return False
        lowest, second_lowest = nums[0], None
        for i, num in enumerate(nums[1:], 1):
            if num > lowest:
                second_lowest = num
                break
            else:
                lowest = num
        if second_lowest is None:
            return False
        little = lowest
        for num in nums[i + 1:]:
            if num > second_lowest:
                return True
            elif num > lowest:
                second_lowest = num
            else:
                if num > little:
                    lowest, second_lowest = little, num
                else:
                    little = num
        return False


s = Solution()
s.increasingTriplet([1,0,0,0,-1,0,0,0,100])