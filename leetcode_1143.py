class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        le_1 = len(text1)
        le_2 = len(text2)

        dp_table = [[0] * (le_2 + 1) for _ in range(le_1 + 1)]
        for i in range(1, le_1 + 1):
            dp_table[i][1] = 1
        for j in range(1, le_2 + 1):
            dp_table[1][j] = 1


        for i in range(1, le_1 + 1):
            for j in range(1, le_2 + 1):
                if text1[i] == text2[j]:
                    dp_table[i][j] = dp_table[i-1][j-1] + 1
                else:
                    dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])

        return dp_table[-1][-1]

