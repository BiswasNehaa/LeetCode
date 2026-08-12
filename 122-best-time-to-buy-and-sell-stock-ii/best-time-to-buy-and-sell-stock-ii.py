class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit= 0

        for j in range(1,len(prices)):
            if (prices[j]>prices[j-1]):
                profit = profit+ (prices[j]-prices[j-1])

        return profit