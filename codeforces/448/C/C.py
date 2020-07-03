#!/usr/bin/env pypy3

import math

MODULUS = 10**9+7

def make_nCr_mod(max_n=2 * 10**5, mod=10**9 + 7):
    max_n = min(max_n, mod - 1)

    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod

    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def nCr_mod(n, r):
        res = 1
        while n or r:
            a, b = n % mod, r % mod
            if a < b:
                return 0
            res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
            n //= mod
            r //= mod
        return res

    return nCr_mod

nCr_mod = make_nCr_mod()

class Sieve:
    def __init__(self, n=10**3):
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

PRIMES = [p for p in sieve.PRIMES if p <= 70]

from collections import Counter
from functools import lru_cache

@lru_cache(None)
def ss_repr(num):
    if num == 1: return 0
    factors = sorted(sieve.fastfactorize(num))
    arr = [0]*19
    for f in factors:
        arr[PRIMES.index(f)] += 1
    arr = [a % 2 for a in arr][::-1]
    arr = int(''.join(map(str,arr)),2)
    return arr

input()

A = input().split(' ')
A = list(map(int, A))

A = Counter(A)

@lru_cache(None)
def even_odd(n):
    even_factor = 0
    odd_factor = 0
    for j in range(0,n+1):
        if j % 2 == 0:
            even_factor += nCr_mod(n, j)
            even_factor = even_factor % MODULUS
        else:
            odd_factor += nCr_mod(n, j)
            odd_factor = odd_factor % MODULUS
    return even_factor, odd_factor

import array

memo = array.array('i', [-1]*71*2**19)

def ans(i, target):
    # number of ways to make target using only [0...i]

    assert(0 <= target < 2**20)
    assert(0 <= i <= 71)

    if memo[i*2**19+target] != -1: return memo[i*2**19+target]

    if i == 1 and target == 0: 
        return pow(2, (A[0] + A[1]), MODULUS)
    if i == 1:
        return 0

    n = A[i]

    even_factor, odd_factor = even_odd(n)
        
    ret = (odd_factor*ans(i-1, target^ss_repr(i)) + even_factor*ans(i-1, target)) % MODULUS

    memo[i*2**19+target] = ret

    return ret

print(ans(70, 0))

# count = 0
# for m in memo:
#     if m != -1: count += 1
        

# print(f"count={count}")