class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        imin, imax = 0, m

        while True:
            i = int((imin + imax) / 2)
            j = int((m + n + 1) / 2) - i
            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1;
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1;
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2:
                    return max_left

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2

s = Solution()
print(s.findMedianSortedArrays([3],[]))
