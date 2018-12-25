class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        思路:  对每一行，遍历每一个数字，
        每一行/列/3x3宫 用字典存储已出现的数字，如果数字在字典中，则返回False
        """
        rows_set = [set() for i in range(9)]
        columns_set = [set() for i in range(9)]  # 不能浅复制list
        three_set = [set() for i in range(9)]

        def tell_three(r, c):
            '''判断当前数字处于第几个3宫格里'''
            r = r // 3
            c = c // 3
            return r * 3 + c

        for r, row in enumerate(board):
            for c, num in enumerate(row):
                if num == '.':
                    continue
                three = tell_three(r, c)
                if num in rows_set[r] or num in columns_set[c] or num in three_set[three]:
                    return False
                else:
                    rows_set[r].add(num)
                    columns_set[c].add(num)
                    three_set[three].add(num)
        return True


# method 2   改进计算三宫格位置
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        思路:  对每一行，遍历每一个数字，
        每一行/列/3x3宫 用字典存储已出现的数字，如果数字在字典中，则返回False
        """
        rows_set = [set() for i in range(9)]
        columns_set = [set() for i in range(9)]  # 不能浅复制list
        three_set = [set() for i in range(9)]

        for r, row in enumerate(board):
            three = r // 3 * 3
            for c, num in enumerate(row):
                if num == '.':
                    continue
                index = three + c // 3
                if num in rows_set[r] or num in columns_set[c] or num in three_set[index]:
                    return False
                else:
                    rows_set[r].add(num)
                    columns_set[c].add(num)
                    three_set[index].add(num)
        return True


# method 3   降低空间复杂度和时间复杂度的做法
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        思路：
            将每一行，每一列，每一个三宫格都转为每一个area来处理
            利用set，判断转换为set后的area是否发生了长度变化
        """

        def tell_valid_area(area):
            # new_area = [a for a in area if a != '.']
            new_area = list(filter(lambda x: x != '.', area))
            return len(new_area) == len(set(new_area))

        def tell_valid_row():
            for row in board:
                if not tell_valid_area(row):
                    return False
            return True

        def tell_valid_column():  # 利用zip函数转制矩阵
            for column in zip(*board):
                if not tell_valid_area(column):
                    return False
            return True

        def tell_valid_three():
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    area = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not tell_valid_area(area):
                        return False
            return True

        return tell_valid_column() and tell_valid_row() and tell_valid_three()
