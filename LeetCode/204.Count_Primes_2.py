class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if primes[i] == True:
                for j in range(i + i, n, i):
                    primes[j] = False

        return sum(primes)
