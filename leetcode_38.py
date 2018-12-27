class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        思路： 理解清楚题意：   1 读作一个1  则下一个数是  11， 11读作两个1， 则下一个数是21， 21读作一个2一个1
        重点在于 如果出现相同的数排在一起，则先读量词，在读这个数
        """
        cur, i = '1', 1
        while i < n:
            amount, now = 1, ''  # 当前数字出现的次数
            for j, l in enumerate(cur[1:]):
                if cur[j] == l:
                    amount += 1
                else:
                    now = now + str(amount) + cur[j]
                    amount = 1
            now = now + str(amount) + cur[-1]  #加上尾部数字
            cur = now
            i += 1
        return cur

s = Solution()
print(s.countAndSay(4))
