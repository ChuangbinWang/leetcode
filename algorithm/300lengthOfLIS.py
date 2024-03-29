class Solution:
	    def lengthOfLIS(self, nums: List[int]) -> int:
			if len(nums) <= 1:
				return len(nums)
			dp = [1 for i in range (len(nums))] 
			for i in range(1, len(nums)):
				for j in range(0, i):
					if nums[j] < nums[i]:
						dp[i] =  max(dp[j] + 1, dp[i])
			return max(dp)
