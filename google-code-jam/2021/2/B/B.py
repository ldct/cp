#!/usr/bin/env pypy3

from __future__ import division, print_function

from functools import lru_cache

import itertools
import sys
import math

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import math

import math

class Sieve:
    def __init__(self, n=10**6+100):
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

def divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def ans(N):
    ret = -1
    for n in range(1, N+1):
        ret = max(ret, deepest(n, N))
    return ret

@lru_cache(None)
def deepest2(N, budget):
    if budget < 0: return float("-inf")
    if budget == 0: return 0

    ret = float("-inf")

    for i in range(2, 10**6):
        if N*i > budget: break
        ret = max(ret, 1+deepest2(N*i, budget-N*i))

    return ret

def ans2(N):
    ret = -2
    for p in range(3, N+1):
        if N-p < 0: break
        old_ret = ret
        ret = max(ret, deepest2(p, N-p))
    return 1+ret

@lru_cache(None)
def deepest(D, S):
    if D == S: return 1
    if D > S: return float("-inf")
    ret = float("-inf")

    for d in divisors(D):
        if d < 3: continue
        if d == D: continue
        ret = max(ret, 1+deepest(d, S-D))
    return ret

if False:
    for n in range(3, 100):
        assert(ans(n) == ans2(n))
else:
    T = int(input())
    for t in range(T):
        N = read_int()
        print("Case #" + str(t+1) + ": " + str(ans2(N)))
print(deepest2.cache_info())