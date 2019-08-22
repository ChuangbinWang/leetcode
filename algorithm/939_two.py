class Solution(object):
    def minAreaRect(self, points):
        pointSet = []
        for x, y in points:
            pointSet.append(4001 * x + y)

        ans = float('inf')
        for a in range(len(points)):
            for b in range(a + 1, len(points)):
                if points[a][0] != points[b][0] and points[a][1] != points[b][1]:
                    if (points[a][0] * 4001 + points[b][1]) in pointSet and (points[b][0] * 4001 + points[a][1]) in pointSet:
                        ans = min(ans, abs(points[a][0] - points[b][0]) * abs(points[a][1] - points[b][1]))

        return ans if ans < float('inf') else 0

class Solution {
    public int minAreaRect(int[][] points) {
        Set<Integer> pointSet = new HashSet();
        for (int[] point: points)
            pointSet.add(40001 * point[0] + point[1]);

        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < points.length; ++i)
            for (int j = i+1; j < points.length; ++j) {
                if (points[i][0] != points[j][0] && points[i][1] != points[j][1]) {
                    if (pointSet.contains(40001 * points[i][0] + points[j][1]) &&
                            pointSet.contains(40001 * points[j][0] + points[i][1])) {
                        ans = Math.min(ans, Math.abs(points[j][0] - points[i][0]) *
                                            Math.abs(points[j][1] - points[i][1]));
                    }
                }
            }

        return ans < Integer.MAX_VALUE ? ans : 0;
    }
}