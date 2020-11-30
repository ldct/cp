#!/usr/bin/env pypy3

from collections import defaultdict, Counter

import math

class Sieve:
    def __init__(self, n=10**7+100):
        self.N = n

        s = [-1] * n
        for i in range(2, int(n**0.5)+1):
            if s[i] != -1: continue
            for j in range(i, n, i):
                if j > i: s[j] = i
        self.s = s

        self.PRIMES = self.primes()
        # print(len(self.PRIMES))

    def primes(self):
        return [i for i, e in enumerate(self.s) if e == -1 and i >= 2]

    def fastfactorize(self, n):
        assert(n <= self.N)

        ret = []

        while self.s[n] != -1:
            ret += [self.s[n]]
            n = n // self.s[n]

        if n > 1:
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

    def factorize(self, n):
        if n < self.N:
            return self.fastfactorize(n)

        for p in self.PRIMES:
            if p*p > n:
                break
            if n % p == 0:
                return [p] + self.factorize(n // p)

        if n == 1: return []
        return [n]

sieve = Sieve()

input()
A = list(map(int, input().split()))

chains = defaultdict(list)

for a in A:
    factors = sieve.factorize(a)
    cf = Counter(factors)

    for p in cf:
        chains[p] += [cf[p]]

def bf(A):
    ret = 1
    for i in range(len(A)):
        for j in range(i, len(A)):
            for k in range(i, j+1):
                ret *= A[k]
    return ret

print(bf([1,3,1,1]))
print(bf([3,1,1,1]))