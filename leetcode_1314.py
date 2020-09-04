class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]

        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return P[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + K + 1, j + K + 1) - get(i - K, j + K + 1) - get(i + K + 1, j - K) + get(i - K,
                                                                                                            j - K)
        return ans
