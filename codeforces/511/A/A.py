#!/usr/bin/env pypy3

import io, os, sys
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache


class Sieve:
    def __init__(self, n=int(1.5e7+100)):
        self.N = n

        s = [-1] * n
        for i in range(2, int(n**0.5)+1):
            if s[i] != -1: continue
            for j in range(i, n, i):
                if j > i: s[j] = i
        self.s = s

    def fastfactorize_counter(self, n):

        _n = n
        while _n % 2 == 0:
            _n //= 2

        ret = []

        while self.s[n] != -1:
            p = self.s[n]

            e = 0
            while n % p == 0:
                e += 1
                n //= p
            ret += [(p, e)]

        if n > 1:
            ret += [(n, 1)]

        return ret

    def fastfactorize(self, n, exclude_duplicates=False):
        assert(n <= self.N)

        ret = []

        while self.s[n] != -1:
            p = self.s[n]
            ret += [p]
            if exclude_duplicates:
                while n % p == 0:
                    n = n // p
            else:
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

        return [n]

sieve = Sieve()

### CODE HERE

input()
A = read_int_list()
N = len(A)

prime_counts = defaultdict(list)

for a in A:
    factors = sieve.fastfactorize_counter(a)
    for p, e in factors:
        prime_counts[p] += [e]

def score(p):
    lst = prime_counts[p]

    if len(lst) < N:
        return N - len(lst)

    mv = min(lst)
    ret = 0
    for e in lst:
        if e == mv:
            ret += 1

    return ret

ret = float("inf")

for p in prime_counts.keys():
    ret = min(ret, score(p))

if ret >= N:
    ret = -1
print(ret)