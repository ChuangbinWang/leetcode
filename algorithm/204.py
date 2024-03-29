class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        isPrimes = [1] * n
        isPrimes[0] = isPrimes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrimes[i] == 1:
                isPrimes[i*i :n :i] = [0] * len(isPrimes[i*i: n : i])
        return sum(isPrimes)