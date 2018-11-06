class Solution:
    def convert(self, s, numRows):

        if numRows == 1:
            return s

        rows = []
        for j in range(numRows):
            rows.append('')
        j = 0
        direction = True
        for i in range(len(s)):
            if j == numRows or j < 0:
                direction = not direction
                if j == numRows:
                    j = j - 2
                    rows[j] += s[i]
                    j -= 1
                else:
                    j = j + 2
                    rows[j] += s[i]
                    j += 1
            elif direction:
                rows[j] += s[i]
                j += 1
            else:
                rows[j] += s[i]
                j -= 1

        z_s = ''
        for row in rows:
            z_s += row

        return z_s


solution = Solution()
print(solution.convert('PAsd', 2))
