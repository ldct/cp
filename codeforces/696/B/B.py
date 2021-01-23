#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())


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

### CODE HERE

def divisors(n):
    ret = []
    for i in range(1, n+1):
        if n % i == 0:
            ret += [i]
    return ret

def ok(r, k):
    d = sorted(divisors(r))
    if len(d) < 4: return False
    for i in range(len(d)-1):
        if not (d[i+1] - d[i] >= k):
            return False
    return True

def ans_slow(d):
    for r in range(1, 10000):
        if ok(r, d):
            return r

from collections import defaultdict

sieve = Sieve()
prime_of = [-1]*30000

for p in sieve.PRIMES:
    if p-1 >= len(prime_of): break
    prime_of[p] = p

last = -1
for i in range(len(prime_of)-1, -1, -1):
    if prime_of[i] != -1:
        last = prime_of[i]
    prime_of[i] = last

def ans(d):
    p = prime_of[d+1]
    q = prime_of[p+d]
    return p*q

for _ in range(read_int()):
    d = read_int()
    print(ans(d))