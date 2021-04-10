#!/usr/bin/env pypy3

from __future__ import division, print_function

import itertools
import sys
import array
from collections import Counter

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

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

from collections import defaultdict

def ans(data):
    S = 0
    freq = defaultdict(int)
    for p, n in data:
        freq[p] = n
        S += p*n

    def ok(cff):
        for k in cff:
            if freq[k] < cff[k]:
                return False
        return True

    ret = 0

    for s in range(S, 1, -1):
        ff = sieve.fastfactorize(s)
        if s + sum(ff) == S:
            cff = Counter(ff)
            if not ok(cff):
                continue
            ret = s
            break

    return ret

T = read_int()
for t in range(T):
    M = read_int()
    data = []
    for _ in range(M):
        data += [read_int_tuple()]
    print("Case #" + str(t+1) + ": " + str(ans(data)))
