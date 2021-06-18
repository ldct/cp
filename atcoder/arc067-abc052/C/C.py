#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())


import math

class Sieve:
    def __init__(self, n=10**3+100):
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

### CODE HERE

from collections import defaultdict

f = defaultdict(int)

N = read_int()
for i in range(2, N+1):
    for p in sieve.fastfactorize(i):
        f[p] += 1

ans = 1
for k in f:
    ans *= (f[k]+1)
    ans %= (10**9+7)

print(ans)