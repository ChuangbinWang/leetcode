class Solution:
    def maxProfit(self, prices) :
        if not prices:
            return 0
        res = 0
        profit = [[0 for i in xrange(3)] for i in xrange(len(prices))]
        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0
        for i in range(1, len(prices)):
            profit[i][0] = profit[i - 1][0]
            profit[i][1] = max(profit[i - 1][1], profit[i - 1][0] - prices[i])
            profit[i][2] = profit[i - 1][1] + prices[i]
            res = max(res, profit[i][0], profit[i][1], profit[i][2])
        return res