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

        self.PRIMES = self.primes()
    
    def primes(self):
        return [i for i, e in enumerate(self.s) if e == -1 and i >= 2]

    def fastfactorize(self, n):
        assert(n <= self.N)

        ret = []

        while self.s[n] != -1:
            ret += [self.s[n]]
            n = n // self.s[n]

        ret += [n]

        return ret

    def factorize(self, n):
        if n < self.N:
            return self.fastfactorize(n)
        
        for p in self.PRIMES:
            if n % p == 0:
                return [p] + self.factorize(n // p)

        return [n]

sieve = Sieve(10**5)

T = int(input())

def largest2(N):
    for i in range(1, 1000000):
        if N % (2**i) != 0:
            return i-1

def ans(N):
    k = largest2(N)
    if k >= 2:
        odd = N // (2**k)
        if odd > 1:
            return "Ashishgup"
        else:
            return "FastestFinger"
    if k == 1:
        odd = N // 2
        # assert(odd % 2 == 1)

        factors = sieve.factorize(odd)

        # assert(len(factors) >= 1)
        if factors == [1]:
            return "Ashishgup"
        if len(factors) == 1:
            return "FastestFinger"
        else:
            return "Ashishgup"

        return '?'

    # assert(k == 0)
    
    odd = N

    if odd > 1:
        return("Ashishgup")
    else:
        # assert(odd == 1)
        return("FastestFinger")

    # assert(False)

for _ in range(T):
    N = int(input())
    print(ans(N))