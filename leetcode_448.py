# method1  暴力 超时
class Solution:
    def findDisappearedNumbers(self, nums):
        res = []
        for i in range(1, len(nums) + 1):
            if i not in nums:
                res.append(i)

        return res


# method2 改进的暴力 超时
class Solution:
    def findDisappearedNumbers(self, nums):
        set_num = set(nums)
        res = []
        max, num = len(res) - len(set_num), 0
        for i in range(1, len(nums) + 1):
            if i not in nums:
                res.append(i)
                num += 1

            if num == max:
                break

        return res


class Solution:

    def findDisappearedNumbers(self, nums):
        # 思路： 遍历，将当前数-1 下标对应的数改为None
        # 遍历完后，nums中不为None的对应下标+1，则为消失的数
        copy_nums = nums.copy()
        for n in nums:
            if n:
                copy_nums[n - 1] = None

        res = []
        for i, n in enumerate(copy_nums):
            if n:
                res.append(i + 1)

        return res


# Excellect code     O[1] , 不使用额外空间
class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        n = len(nums)
        s = set(nums)
        return [i for i in range(1, n+1) if not i in s]