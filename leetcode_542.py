class Solution:
    def updateMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        '''
            思路：
                暴力解法
        '''
        le_r = len(matrix)
        le_c = len(matrix[0])
        from collections import deque

        def helper(i, j):
            queue = deque()
            queue.append([i, j, 0])
            while queue:
                a, b, dis = queue.popleft()
                if matrix[a][b] == 0:
                    return dis
                else:
                    dis += 1
                    if a < le_r - 1:
                        queue.append([a + 1, b, dis])
                    if a > 0:
                        queue.append([a - 1, b, dis])
                    if b < le_c - 1:
                        queue.append([a, b + 1, dis])
                    if b > 0:
                        queue.append([a, b - 1, dis])

        res = []
        for i, row in enumerate(matrix):
            res.append([])
            for j, n in enumerate(row):
                if n == 0:
                    d = 0
                else:
                    d = helper(i, j)
                res[i].append(d)
        return res
