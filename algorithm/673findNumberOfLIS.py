class Solution(object):
    def findNumberOfLIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        dp = [1 for i in range (len(nums))]
        totals = [0 for i in range(0, len(nums) + 1)]
        # totals[1] = len(nums)
        # totals[len(nums)] = 0
        # print "len(nums) + 1)", len(nums) + 1, len(totals)
        for i in range(1, len(nums)):
            for j in range(0, i):
                print nums[i], nums[j]
                if nums[j] < nums[i]:
                    dp[i] =  max(dp[j] + 1, dp[i])
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        totals[dp[i]] += dp[j]
                    elif dp[j] + 1 <= dp[i]:
                        totals[dp[i]] += 1
                elif nums[j] == nums[i]:
                    dp[i] = dp[j]
                    print dp[i]
                    totals[dp[i]] += 1
        # for m in range(0, len(nums) + 1):
            # print "totals[m]11", m , totals[m]
        for m in range(0, len(nums) + 1)[::-1]:
            # print "totals[m]", m , totals[m]
            if totals[m] > 0:
                return totals[m]

if __name__ == "__main__":
    # test = [1, 3, 5, 4, 7]
    test = [2, 2, 2, 2, 2]
    # test = [1,2,4]
    ret = Solution().findNumberOfLIS(test)
    print (ret)





# class Solution(object):
#     def findNumberOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         l = len(nums)
#         dq = list()
#         totals = list()
#         for num in nums:
#             index = len(dq)-1
#             if not dq or num >dq[-1]:
#                 dq.append(num)
#                 totals.append(collections.defaultdict(int))
#             else:
#                 while index >= 0 and dq[index]>= num:
#                     index -= 1
#                 dq[index+1] = num
#             if not index+1:
#                 totals[index+1][num] +=1
#             else:
#                 totals[index+1][num] += sum([val for key,val in totals[index].items() if key <num ])
#         return sum(totals[-1].values())