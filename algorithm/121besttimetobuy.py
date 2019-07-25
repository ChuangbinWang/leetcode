class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        cost, profit = prices[0], 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit


if __name__ == "__main__":
    prices = [2, 1, 4]
    max_profit = Solution().maxProfit(prices)
    print(max_profit)