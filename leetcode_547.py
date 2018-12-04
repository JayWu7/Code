class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int"""
        circles, in_circle = [], set()

        def find_friends(m, n):
            nonlocal circle
            if M[m][n] == 1:
                circle.append((m, n))
                M[n][m], M[m][n] = 0, 0
                in_circle.add(m)
                in_circle.add(n)
            if 1 in M[m]:
                find_friends(m, M[m].index(1))
            if 1 in M[n]:
                find_friends(n, M[n].index(1))

        for i, row in enumerate(M):
            M[i][i] = 0
            if 1 not in row and i not in in_circle:
                circles.append(i)  # 没有朋友，自己一个人独占一个朋友圈
                continue
            elif 1 in row:
                circle = []
                find_friends(i, row.index(1))
                circles.append(circle)
            else:
                continue
        return len(circles)


s = Solution()
print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

#Excellent code
# class Solution:
#     def findCircleNum(self, M):
#         """
#         :type M: List[List[int]]
#         :rtype: int
#         """
#         def dfs(k):
#             if M[k][k] == 0:return
#             M[k][k] = 0
#             for i in range(L):
#                 if M[k][i]:
#                     dfs(i)
#         ans, L = 0, len(M)
#         for i in range(L):
#             if M[i][i]:
#                 ans += 1
#                 dfs(i)
#         return ans
