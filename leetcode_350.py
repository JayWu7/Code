# method 1   针对排序好的数组
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        result = []

        length1 = len(nums1)
        length2 = len(nums2)
        index_1 = index_2 = 0
        while index_1 < length1 and index_2 < length2:
            if nums1[index_1] == nums2[index_2]:
                result.append(nums1[index_1])
                index_1 += 1
                index_2 += 1
            elif nums1[index_1] < nums2[index_2]:
                index_1 += 1
            else:
                index_2 += 1
        return result


# method 2, nums1比nums2小很多
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums1:
            if num in nums2:
                nums2.remove(num)
                result.append(num)
        return result




