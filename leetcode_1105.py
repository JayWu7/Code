class Solution:
    def minHeightShelves(self, books, shelf_width):
        # 一维dp
        dp = [0] + [1000 * 1000 for _ in range(len(books))]

        for i in range(len(dp)):
            cur_width = h = 0
            for j in range(i, 0, -1):
                cur_width += books[j - 1][0]
                if cur_width > shelf_width:
                    break
                h = max(h, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + h)
        return dp[-1]


books = [[1, 3], [2, 4], [3, 2]]
w = 6

S = Solution()
print(S.minHeightShelves(books, w))
