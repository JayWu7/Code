class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        '''
        思路： 纯暴力
        时间： 5 min
        '''
        res = []
        for num in nums1:
            ind = nums2.index(num)
            for n in nums2[ind:]:
                if n > num:
                    res.append(n)
                    break
            else:
                res.append(-1)
        return res

# Excellent code
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dmap = {}
        stack = []

        for n2 in nums2:
            while stack and stack[-1] < n2:
                dmap[stack.pop()] = n2
            stack.append(n2)

        return [dmap.get(n1, -1) for n1 in nums1]