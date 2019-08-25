class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        dp[0] = 0
        if n <= 2:
            return dp[n]
        print (n)
        for i in range(3, n+1):
            print "i = ", i
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            print "i = ", (i), "dp[i]" , (dp[i])
        return dp[n]


if __name__ == "__main__":
    max_profit = Solution().tribonacci(4)
    print(max_profit)