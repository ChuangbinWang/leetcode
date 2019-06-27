class Solution:
    def threeSum(self, nums:List[int])->List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        d = []
        for i, v in enumerate(nums):
            if i > 1 and nums[i] == nums[i-1]:
                continue
            d.append(v)
        for i, v in enumerate(nums[:-2]):
            if i > 1 and nums[i] == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if (-v-x) in d:
                    res.append(v, x , -x-v)
        return res