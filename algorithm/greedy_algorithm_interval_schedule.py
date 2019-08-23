class Solution(object):
    def interval_scheduling(self, interval):
        interval.sort(key=lambda x:x[1])
        count = 1
        x_end = interval[0][1]
        for x, y in interval:
            if x >= x_end:
                x_end = y
                count += 1
        return count

if __name__ == "__main__":
    intvs=[[1,3],[2,8],[3,6]]
    count = Solution().interval_scheduling(intvs)
    print(count)