#!/usr/bin/env pypy3

import io, os, sys
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd, sqrt
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

from fractions import Fraction

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

MODULUS = 10**9+7

def egcd(a, b):
    """
    returns
    gcd(a, b), s, r
    s.t.
    a * s + b * r == gcd(a, b)
    """
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0

def modinv(a, m=MODULUS):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = egcd(a % m, m)
    return x % m if g == 1 else None

### CODE HERE

def divisors(n):
    ret = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            ret += [i]
            if i*i != n:
                ret += [n // i]
    return ret

@lru_cache(None)
def ans_slow(n, k):
    if k == 0:
        return n
    ep = []
    for d in divisors(n):
        ep += [ans_slow(d, k-1)]
    return sum(ep) / Fraction(len(ep))

def ans_pe(p, e, k):
    if k == 0:
        return pow(p, e, MODULUS)
    ep = []
    for f in range(0, e+1):
        ep += [ans_pe(p, f, k-1)]

    # return sum(ep) / len(ep)
    ret = sum(ep) % MODULUS
    ret *= modinv(len(ep))
    ret %= MODULUS
    return ret

@lru_cache(None)
def ans(n, k):
    factors = Counter(Sieve().factorize(n))

    ret = 1
    for p in factors:
        e = factors[p]
        ret *= ans_pe(p, e, k)
        ret %= MODULUS

    return ret

print(ans_pe(5, 10, 10))
# print(ans(*read_int_tuple()))