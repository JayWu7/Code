class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        '''
        思路: 左下角的元素是这一行最小的，同时也是这一列最大的元素
        比较左下角元素和目标值的大小：
            如果一样，则返回True
            如果小，则去掉这一列
            如果大，则去掉这一行
            如果最后数组为空，则返回False
        '''
        """
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False
