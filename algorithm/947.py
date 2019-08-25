# class Solution {
#     public int removeStones(int[][] stones) {
#         int N = stones.length;
#         DSU dsu = new DSU(20000);

#         for (int[] stone: stones)
#             dsu.union(stone[0], stone[1] + 10000);

#         Set<Integer> seen = new HashSet();
#         for (int[] stone: stones)
#             seen.add(dsu.find(stone[0]));

#         return N - seen.size();
#     }
# }

# class DSU {
#     int[] parent;
#     public DSU(int N) {
#         parent = new int[N];
#         for (int i = 0; i < N; ++i)
#             parent[i] = i;
#     }
#     public int find(int x) {
#         if (parent[x] != x) parent[x] = find(parent[x]);
#         return parent[x];
#     }
#     public void union(int x, int y) {
#         parent[find(x)] = find(y);
#     }
# }

class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        N = len(stones)
        dsu = DSU(N)
        for x, y in stones:
            dsu.union(x, y + 10000)
        return N - len({dsu.find(x) for x, y in stones})