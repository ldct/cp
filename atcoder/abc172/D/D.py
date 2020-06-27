#!/usr/bin/env pypy3

import math
from collections import Counter
import array

class Sieve:
    def __init__(self, n=10**7+100):
        self.N = n

        self.nd = array.array('i', [1] * n)

        for i in range(2, n):
            for j in range(i, n, i): 
                self.nd[j] += 1
    
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

    def isprime(self, n):
        if n < self.N:
            return self.s[n] == -1
        for p in self.PRIMES:
            if p*p > n:
                return True
            if n % p == 0:
                return False

    def numDivisors(self, n):
        if n == 1: return 1

        c = dict()

        for f in self.fastfactorize(n):
            if f not in c: c[f] = 0
            c[f] += 1

        ret = 1
        for p in c:
            ret *= (c[p] + 1)
        return ret

    def factorize(self, n):
        if n < self.N:
            return self.fastfactorize(n)
        
        for p in self.PRIMES:
            if p*p > n:
                break
            if n % p == 0:
                return [p] + self.factorize(n // p)

        return [n]

N = int(input())

sieve = Sieve()

ans = 0

for k in range(1, N+1):
    ans += k*sieve.nd[k]

print(ans)
