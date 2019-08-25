class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points or len(points) == 0:
            return 0
        points.sort(key=lambda x:x[1])
        count = 1
        x_end = points[0][1]
        for x, y in points:
            if x > x_end:
                count += 1
                x_end = y
        return count