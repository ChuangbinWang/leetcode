class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        windows , res = [], []
        for i, x in enumerate(nums):
            if i >= k and windows[0] <= i - k:
                windows.pop(0)
            while windows and x >= nums[windows[-1]]:
                windows.pop()
            windows.append(i)
            if i >= k - 1:
                res.append(nums[windows[0]])
        return res