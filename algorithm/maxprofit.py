class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for x in range(len(prices)-1):
            differ = prices[x+1] - prices[x]
            if differ > 0:
                profit += differ
        return profit