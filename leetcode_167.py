class Solution(object):
    def twoSum(self, numbers, target):
        """
        思路: 双指针
        time： 5min
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        le, ri = 0, len(numbers) - 1
        while le < ri:
            cur = numbers[le] + numbers[ri]
            if cur < target:
                le += 1
            elif cur > target:
                ri -= 1
            else:
                return [le + 1, ri + 1]
