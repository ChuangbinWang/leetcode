class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n :
            count += n & 1
            n >> 1
        if count == 1:
            return True
        else:
            return False