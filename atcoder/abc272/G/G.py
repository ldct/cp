#!/usr/bin/env python3
 
from concurrent.futures import thread
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
 
def mf(c):
    ret = 0
    for k in c:
        ret = max(ret, c[k])
    return ret
 
def works_slow(p, A):
    if p <= 2: return False
    c = Counter([a % p for a in A])
    return mf(c) > len(A) // 2
 
def works_fast(p, A):

    if len(A) >= 10000:
        AA = A[0:20]
        AA = Counter([a % p for a in AA])
        if mf(AA) <= 3: return False


    return works_slow(p, A)

    if p <= 2: return False
    c = Counter([a % p for a in A])
    return c[target] > len(A) // 2

def ans(A):    
 
    for p in [4]:
        if works_slow(p, A):
            return p
  
    for _ in range(60):
        a = random.choice(A)
        b = random.choice(A)
        M = abs(b-a)
 
        for p in sieve.factorize(M):
            if p == 0:
                return -1
            if p > 2 and works_fast(p, A):
                return p
    return -1

input()
A = read_int_list()
random.shuffle(A)

print(ans(A))