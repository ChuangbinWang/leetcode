class Solution(object):
    def coinChange(self, coins, amount):
        dp = [(amount + 1) for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], dp[i] - j + 1)
                    print(i, j, dp[i])
        if dp[amount] > amount :
            return -1 
        else :
            return dp[amount]

if __name__ == "__main__":
    prices = [1, 2, 5]
    max_profit = Solution().coinChange(prices, 11)
    print(max_profit)