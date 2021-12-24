#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

### CODE HERE

from functools import lru_cache

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

@lru_cache(None)
def ans_set(s):
    ret = 0
    for a in s:
        for b in s:
            if a == b: continue
            if gcd(a, b) == 1: continue
            ret = max(ret, 1 + ans(s - frozenset([a, b])))
    return ret

def ans_greedy(s):
    primes = [p for p in sieve.PRIMES if p*p <= 10**5][::-1]
    ret = 0
    matched = [False]*(s+1)

    for p in primes:
        halfs = 0
        for i in range(1, s+1):
            if i % p == 0 and not matched[i]:
                halfs += 1
                matched[i] = True
        if halfs > 0:
            print(f"for prime {p} matched {halfs}")
        ret += halfs//2

    return ret

print(ans_greedy(9))
