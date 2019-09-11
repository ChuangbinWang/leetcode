class Solution(object):
    def trap(self, height):
        if len(height) == 0: return 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[0], height[len(height) - 1]
        ans = 0
        while left <= right:
            l_max = max(height[left], l_max)
            r_max = max(r_max, height[right])
            if l_max < r_max:
                ans += l_max - height[left]
                left += 1
            else:
                ans += r_max - height[right]
                right -= 1
        return ans