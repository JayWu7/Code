class Solution(object):
    def islandPerimeter(self, grid):
        """
        思路：递归
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = [[0] * (len(grid)+1) + grid] + [[0] + row for row in grid]

