class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        思路： 先计算第一个数字和第二个数字有多少种组合，然后再计算第一和第二 和 第三个数字的组合
        """
        if not digits:
            return []
        digit_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if len(digits) == 1:
            return digit_dict[digits[0]]

        def helper(left, cur):
            l1 = len(left)
            l2 = len(cur)
            res = []
            for i in left:
                for j in cur:
                    res.append(i + j)
            return res

        res = digit_dict[digits[0]]
        for d in digits[1:]:
            res = helper(res, digit_dict[d])

        return res