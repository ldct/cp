#!/usr/bin/env pypy3

from collections import Counter

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

        return [n]

sieve = Sieve()

def ans(N):
    factors = sieve.factorize(N)
    cf = Counter(factors)
    f = set(factors)

    max_count = max(cf[v] for v in f)
    p = None
    for v in f:
        if cf[v] == max_count:
            p = v
            break

    ret = [p]*(max_count-1)

    pr = 1
    for r in ret:
        pr *= r

    ret += [N // pr]

    print(len(ret))
    print(*ret)

for _ in range(int(input())):
    N = int(input())
    ans(N)
