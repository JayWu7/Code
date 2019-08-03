class Solution(object):
    def spiralOrder(self, matrix):
        """
        思路: 先定义上下左右的边界，每到一个边界，更改遍历方向
        时间：
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        w, s, a, d = 0, len(matrix), 0, len(matrix[0])  # 上下左右边界
        res = []
        row = 0
        while True:
            if a >= d:
                break
            for j in range(a, d):
                res.append(matrix[row][j])
            col = j
            w += 1
            if w >= s:
                break
            for i in range(w, s):
                res.append(matrix[i][col])
            row = i
            d -= 1
            if d <= a:
                break
            for j in range(d - 1, a - 1, -1):
                res.append(matrix[row][j])
            col = j
            s -= 1
            if s <= w:
                break
            for i in range(s - 1, w - 1, -1):
                res.append(matrix[i][col])
            row = i
            a += 1
        return res
