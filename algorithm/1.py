class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        j = -1
        for i in range(1, len(nums)):
            tmp = nums[:i]
            if (target - nums[i]) in tmp:
                j = tmp.index(target - nums[i])
                break
        if j >= 0:
            return [i, j]

if __name__ == "__main__":
    res = Solution().twoSum([2,5,5,11],10)
    print(res)