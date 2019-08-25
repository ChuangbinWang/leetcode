class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pl = []
        ret = [0] * len(S)
        for i in range(0, len(S)):
            if S[i] == C:
                pl.append(i)
        for i in range(0, len(S)):
            minx = 10000000
            for l in range(0, len(pl)):
                minx = min(minx, abs(pl[l] - i))
            ret[i] = minx
        return ret
if __name__ == "__main__":
    S = "loveleetcode"
    C = 'e'
    ret = Solution().shortestToChar(S, C)
    print(ret)