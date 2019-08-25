class Solution(object):
    def interval_scheduling(self, interval):
        if not interval or len(interval) == 0:
            return 0
        interval.sort(key=lambda x:x[1])
        count = 1
        x_end = interval[0][1]
        for x, y in interval:
            if x >= x_end:
                x_end = y
                count += 1
        return count

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        wucongdie = self.interval_scheduling(intervals)
        return len(intervals) - wucongdie        

