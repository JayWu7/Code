class Solution(object):
    def islandPerimeter(self, grid):
        """
        思路：遍历,如果是1，则total_island + 1
            如果下或者右有连接，则decrease + 1
            最后返回  4*total_island - decrease*2
        time: 60min
        速度 544ms，击败百分之百
        :type grid: List[List[int]]
        :rtype: int
        """
        le = len(grid)
        total_island = 0
        decrease = 0
        for i in range(le):
            le_r = len(grid[i])
            for j in range(le_r):
                if grid[i][j]:
                    total_island += 1
                    if i < le - 1 and grid[i + 1][j]:
                        decrease += 1
                    if j < le_r - 1 and grid[i][j + 1]:
                        decrease += 1
        return total_island * 4 - decrease * 2 

