#!/usr/bin/env pypy3

class Sieve:
    def __init__(self, n=10**7):
        self.N = n

        s = [-1] * n
        for i in range(2, int(n**0.5)+1):
            if s[i] != -1: continue
            for j in range(i, n, i): 
                if j > i: s[j] = i
        self.s = s
    
    def primes():
        return [i for i, e in enumerate(self.s) if e == -1 and i >= 2]

    def fastfactorize(self, n):
        assert(n <= self.N)

        ret = []

        while self.s[n] != -1:
            ret += [self.s[n]]
            n //= self.s[n]

        ret += [n]

        return ret

sieve = Sieve()
N = int(input())

ans = 0
for i in range(1, N+1):
    factors = sieve.fastfactorize(i)
    if len(set(factors)) == 2:
        ans += 1

print(ans)