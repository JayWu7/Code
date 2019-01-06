# method 1   时间复杂度： O（m*n）  空间复杂度：  O（m+n）
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        思路： 先遍历矩阵每一行判断0是否在此行，并生成一个列表来记录
                然后以列为单位遍历矩阵，判断每一列是否有0
                最后遍历矩阵每一个数字，如果此数字不为0，且所在行或列存在0，则把此数字置为0
        """
        row_zero = [0 in row for row in matrix]
        column_zero = [0 in column for column in zip(*matrix)]
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and (row_zero[i] or column_zero[j]):
                    matrix[i][j] = 0
