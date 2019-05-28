# method 1
class Solution:
    def twoSum(self, nums, target):
        for i1 in range(len(nums)):
            n1 = nums[i1]
            n2 = target - n1
            if n2 in nums:
                i2 = nums.index(n2)
                if i1 != i2:
                    return [i1, i2]


# method 2
class Solution:
    def twoSum(self, nums, target):
        """ 
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
        思路：
            首先排除target/2 在nums里存在的情况
            字典键存储target-num的值，值存储num的下标
            然后遍历nums，如果num在dict_num里，返回排序后的num下标i和dict_num的num键对应的值
        """
        if target / 2 in nums and nums.count(target / 2) > 1:
            x = nums.index(target / 2)
            y = nums.index(target / 2, x + 1)
            return [x, y]

        dict_nums = {target - num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if num in dict_nums and i != dict_nums[num]:
                return sorted([i, dict_nums[num]])

#excellent code
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = dict()
        for k, v in enumerate(nums):
            if target - v in hash_map:
                return [k, hash_map[target-v]]
            hash_map[v] = k
