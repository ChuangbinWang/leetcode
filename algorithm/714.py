class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        res = 0
        dp = [[0 for i in range(3)] for i in range(len(prices))]
        dp[0][0], dp[0][1], dp[0][2] = -prices[0], 0, 0
        # print "start", (-prices[0]- fee), 0, 0
        for i in range(1, len(prices)):
            # print "day", (i)
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i] - fee
            dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
            res = max(res, dp[i][0], dp[i][1], dp[i][2])
            # print (res), (dp[i][0]), (dp[i][1]), (dp[i][2])
        return res

if __name__ == "__main__":
    prices = [1,3,2,8,4,9]
    max_profit = Solution().maxProfit(prices, 2)
    print(max_profit)