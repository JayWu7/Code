class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        思路：  利用zip函数，
        """
        zip_matrix = list(zip(*matrix))
        for i in range(len(matrix)):
            matrix[i] = list(reversed(zip_matrix[i]))
