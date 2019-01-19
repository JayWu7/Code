class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        mem = [float('inf')]*(amount+1)
        mem[0] = 0
        for coin in coins:
            for j in range(coin, amount+1):
                mem[j] = min(mem[j], mem[j - coin] + 1)

        return -1 if mem[-1] > amount else mem[-1]


s = Solution()
s.coinChange([3,7,405,436]
,8839)