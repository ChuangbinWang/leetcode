    class Solution:
        def maxArea(self, height: List[int]) -> int:
            i, j, res = 0, len(height) - 1, 0
            while j > i:
                area = (j - i) * min(height[i], height[j])
                if area > res:
                    res = area
                if height[i] > height[j]:
                    j -= 1
                else:
                    i += 1
            return res