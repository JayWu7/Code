class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        length = len(candidates)

        def helper(i, nums, nums_sum):
            if nums_sum == target:
                res.append(nums)
            elif nums_sum > target or i == length:
                pass
            else:
                helper(i, nums + [candidates[i]], nums_sum + candidates[i])
                if i < length - 1:
                    nums[-1] = candidates[i + 1]
                    nums_sum += candidates[i + 1] - candidates[i]
                    helper(i + 1, nums, nums_sum)

        helper(0, [candidates[0]], candidates[0])
        return res
