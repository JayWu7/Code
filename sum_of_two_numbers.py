class Solution:
    def twoSum(self, nums, target):
        for i1 in range(len(nums)):
            n1 = nums[i1]
            n2 = target - n1
            if n2 in nums:
                i2 = nums.index(n2)
                if i1 != i2:
                    return [i1, i2]



nums = [2, 7, 11, 15, 13]
target = 20

s=Solution()
a=s.twoSum(nums,target)
print(a)