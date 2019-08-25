class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        left = 0
        ret = [10000] * len(S)
        for right in range(0, len(S)):
            if S[right] == C:
                for i in range(left, right + 1):
                    ret[i] = min(ret[i], right - i)
                left = right
            elif S[left] == C:
                ret[right] = min(ret[right], right - left)
        return ret