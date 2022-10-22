#!/usr/bin/env python3

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
import random

### CODE HERE

class Sieve:
    def __init__(self, n=10**5+100):
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

    def fastfactorize_counter(self, n):
        assert(n <= self.N)

        ret = Counter()

        while self.s[n] != -1:
            p = self.s[n]
            ret[p] += 1
            n = n // self.s[n]

        if n > 1:
            ret[n] += 1

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
# print(sieve.factorize(10**9+7))

def check(p, A):
    if p <= 2: return False
    if works_slow(p, A):
        print(p)
        exit()

def works_slow(p, A):
    c = Counter([a % p for a in A])
    N = len(A)
    threshold = N//2 + 1
    for k in c:
        if c[k] >= threshold:
            return True
    return False



def ans(A):
    for p in [10**9, 4]:
        check(p, A)

    for _ in range(60):
        a = random.choice(A)
        b = random.choice(A)
        dif = abs(b-a)
        for p in set(sieve.factorize(dif)):
            if p == 0:
                return -1

            check(p, A)
    return -1

input()
A = read_int_list()

print(ans(A))