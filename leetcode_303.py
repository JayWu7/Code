class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


# fast method

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        help = [0]
        for i, n in enumerate(nums):
            help.append(n + help[i])
        self.help = help[1:]

    def sumRange(self, i: int, j: int) -> int:
        if not i:
            return self.help[j]
        else:
            return self.help[j] - self.help[i - 1]


# do some improvement in generating self.help list

class NumArray:

    def __init__(self, nums: List[int]):
        self.help, pre = [], 0
        for n in nums:
            self.help.append(n + pre)
            pre = self.help[-1]

    def sumRange(self, i: int, j: int) -> int:
        if not i:
            return self.help[j]
        else:
            return self.help[j] - self.help[i - 1]
