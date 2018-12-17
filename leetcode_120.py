class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        depth = len(triangle)
        minimum = triangle[-1]
        for index in range(depth - 2, -1, -1):
            for i, num in enumerate(triangle[index]):
                minimum[i] = num + min(minimum[i], minimum[i + 1])
        return minimum[0]


s = Solution()
print(s.minimumTotal([[1], [-5, -2], [3, 6, 1], [-1, 2, 4, -3]]))
