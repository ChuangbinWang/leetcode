class DSU:
    def __init__(self, N):
        self.count = N
        self.parent = [i for i in range(N)]
        self.rank = [1 for i in range(N)]
    
    def find(self, p):
        while self.parent[p] != p:
            p = self.parent[p]
            self.parent[p] = self.parent[p]
        return p 

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[q_root] = p_root
            self.rank[p_root] += 1

        self.count -= 1

    def get_count(self):
        return self.count

class Solution(object):
    def findCircleNum(self, M):
        m = len(M)
        dsu = DSU(m)
        for i in range(m):
            for j in range(m):
                if M[i][j] == 1:
                    dsu.union(i,j)

        return dsu.get_count()

if __name__ == "__main__":
    aaa = [[1,1,0],
            [1,1,0],
            [0,0,1]]
    ret = Solution().findCircleNum(aaa)
    print((ret))
