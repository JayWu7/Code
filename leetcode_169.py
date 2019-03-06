class Solution:
    def majorityElement(self, nums):
        count,start = 0, 0
        for num in nums:
            if num == start:
                count += 1
            elif count == 0:
                start = num
            else:
                count -= 1
        return start


class Solution:
    def majorityElement(self, nums):
        res = {}
        for num in nums:
            res[num] = 1 if num not in res else res[num] + 1
        return max(res,key=res.get)
