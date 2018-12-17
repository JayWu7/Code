from cProfile import Profile
from pstats import Stats
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        def tell_square(row_i, column_i):
            side = 1
            try:
                while matrix[row_i][column_i + side] == '1':
                    for l in range(1, side + 1):
                        if matrix[row_i + l][column_i + side] == '0':
                            return side * side
                        for k in range(1, side + 1):
                            if matrix[row_i + l][column_i + side - k] == '0':
                                return side * side
                    side = side + 1
            except IndexError:
                pass
            return side*side

        max_square = 0
        for row_i, row in enumerate(matrix):
            if '1' in row:
                for column_i, column in enumerate(row):
                    if column == '1':
                        max_square = max(max_square,tell_square(row_i,column_i))
        return max_square
profile = Profile()
s = Solution()
a = [["0","0","0","1","0","1","1","1"],["0","1","1","0","0","1","0","1"],["1","0","1","1","1","1","0","1"],["0","0","0","1","0","0","0","0"],["0","0","1","0","0","0","1","0"],["1","1","1","0","0","1","1","1"],["1","0","0","1","1","0","0","1"],["0","1","0","0","1","1","0","0"],["1","0","0","1","0","0","0","0"]]

profile.run('s.maximalSquare(a)')
stats = Stats(profile)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()

#Excellent code
# class Solution(object):
#     def maximalSquare(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """
#         if not matrix:
#             return 0
#         m = len(matrix);n = len(matrix[0])
#         s = [[0]*n for i in range(m)]
#         result = 0
#         for  i in range(n):
#             if matrix[0][i]=='1':
#                 s[0][i]=1
#                 result = 1
#         for i in range(m):
#             if matrix[i][0]=='1':
#                 s[i][0]=1
#                 result = 1
#         for i in range(1,m):
#             for j in range(1,n):
#                 if matrix[i][j]=='1':
#                     s[i][j] = min(s[i-1][j],s[i][j-1],s[i-1][j-1])+1
#                 else:
#                     s[i][j]==0
#                 if s[i][j]>result:
#                     result = s[i][j]
#         return result*result