class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        len_row = len(grid)
        len_column = len(grid[0])

        for i in range(len_row):
            for j in range(len_column):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[i][j]


# method 2
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        last_row = len(grid) - 1
        last_column = len(grid) - 1

        step_stack = [((0, 0), grid[0][0])]

        # 二分插入
        def insert_step(index, weight):
            le, ri = 0, len(step_stack) - 1
            while le < ri:
                mid = (le + ri) // 2
                if step_stack[mid][1] < weight:
                    le = mid + 1
                else:
                    ri = mid
            step_stack.insert((index, weight), le)

        while step_stack:
            step = step_stack.pop()
            if step[0] == (last_row, last_column):
                return step[1]
            else:
                if step[0][0] != last_row:
                    insert_step((step[0][0] + 1, step[0][1]), step[1] + grid[step[0][0] + 1][step[0][1]])
                if step[0][1] != last_column:
                    insert_step((step[0][0], step[0][1] + 1), step[1] + grid[step[0][0]][step[0][1] + 1])

