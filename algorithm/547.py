class Solution(object):
    def findCircleNum(self, M):
        n = len(M)
        p = {i: {i} for i in range(n)}  
        ans = n
        for i in range(n):
            for j in range(i, n):  
                if M[i][j] == 1 and p[i] is not p[j]:
                    p[i] |= p[j]        
                    print(p[i])
                    for k in p[j]:    
                        p[k] = p[i]
                    ans -= 1          
        return ans

if __name__ == "__main__":
    aaa = [[1,1,0],
            [1,1,0],
            [0,0,1]]
    ret = Solution().findCircleNum(aaa)
    print((ret))
