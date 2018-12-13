class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        result,min_price = 0,prices[0]
        for price in prices:
            min_price = min(price,min_price)
            result = max(result,price - min_price)
        return result
s = Solution()
s.maxProfit(
[7,4,1,2])
