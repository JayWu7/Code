# method1  超时
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        end = len(nums) - 1
        if not end:
            return True
        stack = [(0, i) for i in range(1, nums[0] + 1)]
        used = {0}
        while stack:
            cur_route = stack.pop()
            cur = sum(cur_route)
            if cur < end and cur not in used:
                stack.extend([(cur, i) for i in range(1, nums[cur] + 1)])
                used.add(cur)
            elif cur == end:
                return True
        return False


# method2
class Solution:
    def canJump(self, nums):
        '''从后往前，如果有一个数能到达最后一个数，则截断这个数后面的数组
        如果最后数组只含第一个元素，则返回True，否则返回False'''
        length = len(nums)
        index, end, n = length - 2, length - 1, 1
        while index > -1:
            if nums[index] >= n:  # 可以到最后一个点
                end, n = index, 1
            else:
                n += 1
            index -= 1
        return end == 0


