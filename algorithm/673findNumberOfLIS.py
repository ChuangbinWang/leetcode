class Solution(object):
    def findNumberOfLIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        totals = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        totals[i] = totals[j]
                    elif dp[j] + 1 == dp[i]:
                        totals[i] += totals[j]
        ans = 0
        lis = max(dp)
        for i in range(len(nums)):
            if dp[i] == lis:
                ans += totals[i]
        return ans