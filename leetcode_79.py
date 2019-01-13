class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        思路： 首先遍历board，找到word的第一个字母
                然后搜索此字母上下左右是否有word的第二个字母
                    如果有，继续搜索第三个字母
                    如果没有，则重新查找第一个字母
        """

        def find(x, y, index, used):
            if index == len(word):
                return True
            b1 = b2 = b3 = b4 = False
            if x and board[x - 1][y] == word[index] and (x - 1, y) not in used:
                cur_used = used.copy()
                cur_used.add((x - 1, y))
                b1 = find(x - 1, y, index + 1, cur_used)
            if b1: return b1
            if x < len(board) - 1 and board[x + 1][y] == word[index] and (x + 1, y) not in used:
                cur_used = used.copy()
                cur_used.add((x + 1, y))
                b2 = find(x + 1, y, index + 1, cur_used)
            if b2: return b2
            if y and board[x][y - 1] == word[index] and (x, y - 1) not in used:
                cur_used = used.copy()
                cur_used.add((x, y - 1))
                b3 = find(x, y - 1, index + 1, cur_used)
            if b3: return b3
            if y < len(board[x]) - 1 and board[x][y + 1] == word[index] and (x, y + 1) not in used:
                cur_used = used.copy()
                cur_used.add((x, y + 1))
                b4 = find(x, y + 1, index + 1, cur_used)
            if b4: return b4
            return False

        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0]:
                    if find(i, j, 1, {(i, j)}):
                        return True
        return False


# method2
class Solution:
    def exist(self, board, word):
        '''
        思路： 查找出word每个单词在board中出现的位置
        然后遍历word，如果每个字母都能连接起来，则返回true
        '''
        from collections import defaultdict

        letter_dict = defaultdict(list)
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter in word:
                    letter_dict[letter].append((i, j))

        



s = Solution()
s.exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS")
