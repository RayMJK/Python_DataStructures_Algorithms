def solution(n):
    answer = 0
    primes = [True] * (n+1)
    primes[0]=primes[1]=False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if primes[i] == True:
            for j in range(2*i,n+1, i):
                primes[j] = False
    print(primes)
    return sum(primes)

print(solution(4))