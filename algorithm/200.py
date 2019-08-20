class DSU:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [i for i in range(m*n)]
        self.rank = [1 for i in range(m*n)]
        for a in range(m):
            for b in range(n):
                if grid[a][b] == '1':
                    self.count += 1

    def find(self, p):
        while self.parent[p] != p:
            p = self.parent[p]
            self.parent[p] = self.parent[p]
        return p

    def union(self, p, q):
        p_f = self.find(p)
        q_f = self.find(q)
        if p_f == q_f:
            return
        if self.rank[p_f] > self.rank[q_f]:
            self.parent[q_f] = p_f
        elif self.rank[p_f] < self.rank[q_f]:
            self.parent[p_f] = q_f
        else:
            self.parent[q_f] = p_f
            self.rank[p_f] += 1
        self.count -= 1

    def get_count(self):
        return self.count

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        dsu = DSU(grid)
        for a in range(m):
            for b in range(n):
                if grid[a][b] == '0':
                    continue
                for c in direction:
                    x, y = c[0] + a, b + c[1]
                    if x >= 0 and y >= 0 and x < m and y < n and grid[x][y] == '1':
                        dsu.union(a * n + b, x * n + y) 
        return dsu.get_count()

if __name__ == "__main__":
    aaa = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    ret = Solution().numIslands(aaa)
    print((ret))