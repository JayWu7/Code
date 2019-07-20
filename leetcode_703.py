#method1 超时

# class KthLargest(object):
#
#     def __init__(self, k, nums):
#         """
#         :type k: int
#         :type nums: List[int]
#         """
#         self.k = k
#         self.nums = nums
#         self.k_nums = sorted(nums)[-k:]
#
#     def add(self, val):
#         """
#         :type val: int
#         :rtype: int
#         """
#         if len(self.k_nums) < self.k:
#             for i in range(len(self.k_nums)):
#                 if val <= self.k_nums[i]:
#                     break
#                     self.k_nums = self.k_nums[:i] + [val] + self.k_nums[i:]
#             else:
#                 self.k_nums.append(val)
#         elif val > self.k_nums[0]:
#             for i in range(1, self.k):
#                 if val <= self.k_nums[i]:
#                     self.k_nums = self.k_nums[1:i] + [val] + self.k_nums[i:]
#                     break
#             else:
#                 self.k_nums = self.k_nums[1:] + [val]
#         return self.k_nums[0]

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        import heapq
        self.k = k
        self.k_nums = sorted(nums)[-k:]
        heapq.heapify(self.k_nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        import heapq
        if len(self.k_nums) < self.k:
            heapq.heappush(self.k_nums, val)
        elif self.k_nums[0] < val:
            heapq.heapreplace(self.k_nums, val)
        else:
            pass

        return self.k_nums[0]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
obj.add(3)
obj.add(5)
obj.add(10)
obj.add(9)
obj.add(4)
