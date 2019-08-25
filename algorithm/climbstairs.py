class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one_step_before = 2
        twe_step_before = 1
        all_counts = 0
        for i in range(2, n):
            all_counts = one_step_before + twe_step_before
            twe_step_before = one_step_before
            one_step_before = all_counts
        return all_counts