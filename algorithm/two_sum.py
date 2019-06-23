class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [i, hash_map[nums[i]]]
            hash_map[x] = i

        hash_map = dict()
        for i, x in enumerate(nums):
            hash_map[x] = i
            if target - x in hash_map:
                return [i, hash_map[target - x ]]