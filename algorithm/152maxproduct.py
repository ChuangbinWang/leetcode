class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None: return 0
        res, curMax, curMin = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                curMax = max(curMax * nums[i], nums[i])
                curMin = min(curMin * nums[i], nums[i])
            else :
                tmp = curMax
                curMax = max(curMin * nums[i], nums[i])
                curMin = min(tmp * nums[i], nums[i])
            res = max(curMax, res)
        return res
        