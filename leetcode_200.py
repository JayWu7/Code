# class Solution:
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#
#         def helper(x, y):
#             stack = {(x, y)}
#             while stack:
#                 cur = stack.pop()
#                 if grid[cur[0]][cur[1]] == 0:
#                     continue
#                 grid[cur[0]][cur[1]] = 0
#                 if cur[0] and grid[cur[0] - 1][cur[1]] == '1':  # 上一格!= 0
#                     stack.add((cur[0] - 1, cur[1]))
#                 try:
#                     if grid[cur[0] + 1][cur[1]] == '1':  # 下一格!= 0
#                         stack.add((cur[0] + 1, cur[1]))
#                 except IndexError:
#                     pass
#                 if cur[1] and grid[cur[0]][cur[1] - 1] == '1':  # 左一格!= 0
#                     stack.add((cur[0], cur[1] - 1))
#                 try:
#                     if grid[cur[0]][cur[1] + 1] == '1':  # 右一格!= 0
#                         stack.add((cur[0], cur[1] + 1))
#                 except IndexError:
#                     pass
#
#         num = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == '1':
#                     num += 1
#                     helper(i, j)
#         return num


# method 2   修改grid，使没有数组越界的可能
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        def helper(x, y):
            stack = {(x, y)}
            while stack:
                cur = stack.pop()
                if grid[cur[0]][cur[1]] == 0:
                    continue
                grid[cur[0]][cur[1]] = 0
                if grid[cur[0] - 1][cur[1]] == '1':  # 上一格!= 0
                    stack.add((cur[0] - 1, cur[1]))
                if grid[cur[0] + 1][cur[1]] == '1':  # 下一格!= 0
                    stack.add((cur[0] + 1, cur[1]))
                if grid[cur[0]][cur[1] - 1] == '1':  # 左一格!= 0
                    stack.add((cur[0], cur[1] - 1))
                if grid[cur[0]][cur[1] + 1] == '1':  # 右一格!= 0
                    stack.add((cur[0], cur[1] + 1))

        len_column = len(grid[0])
        grid.insert(0, ['0' for _ in range(len_column)])
        grid.append(['0' for _ in range(len_column)])
        num = 0
        for i in range(len(grid)):
            grid[i] = [0] + grid[i] + [0]

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                if grid[i][j] == '1':
                    num += 1
                    helper(i, j)
        return num


s = Solution()
s.numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
