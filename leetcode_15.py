class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        zero_nums = []
        positive_nums = list(set([num for num in nums if num > 0]))
        negative_nums = list(set([num for num in nums if num < 0]))

        set_nums = set()
        dict_len = {}
        for num in nums:
            set_nums.add(num)
            dict_len[num] = dict_len.get(num, 0) + 1

        if 0 in dict_len and dict_len[0] >= 3:
            zero_nums.append([0, 0, 0])

        if not positive_nums or not negative_nums:
            return zero_nums

        positive_nums.sort()
        negative_nums.sort()

        for neg in negative_nums:
            for pos in positive_nums:
                neg_num = -neg - pos
                if neg_num in set_nums:
                    if neg_num in (neg, pos) and dict_len[neg_num] > 1:
                        zero_nums.append([neg, neg_num, pos])
                    elif neg < neg_num <= 0 or neg_num > pos:
                        zero_nums.append([neg, neg_num, pos])
                elif neg_num < negative_nums[0]:
                    break

        return zero_nums


s = Solution()
print(s.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
