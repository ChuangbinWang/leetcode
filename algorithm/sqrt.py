class Solution:
    def mySqrt(self, x: int) -> int:
        # 为了照顾到 0 把左边界设置为 0
        l = 0
        # 为了照顾到 1 把右边界设置为 x // 2 + 1
        r = x // 2 + 1
        while l < r:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            mid = l + (r - l + 1) // 2
            square = mid * mid
            
            if square > x:
                r = mid - 1
            else:
                l = mid
        return l