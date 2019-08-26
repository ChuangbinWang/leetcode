class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -x-v, x))
        return map(list,res)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i+1]:
                continue
            a = i + 1
            b = len(nums) - 1
            while a < b:
                s = nums[a] + nums[b] + nums[i]
                if s > 0:
                    b -= 1
                elif s < 0:
                    a += 1
                else:
                    res.append((nums[i], nums[a], nums[b]))
                    while a < b and nums[a+1] == nums[a]:
                        a += 1
                    while a < b and nums[b-1] == nums[b]:
                        b -= 1
                    a += 1
                    b -= 1
        return res 