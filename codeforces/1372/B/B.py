#!/usr/bin/env pypy3

from math import gcd
import math

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

def lcm(a, b):
    return a*b // gcd(a, b)

def ans_slow(n):
    
    smallest_lcm = float("inf")
    smallest_pair = None

    for a in range(1,n):
        b = n - a
        if lcm(a, b) < smallest_lcm:
            smallest_lcm = lcm(a, b)
            smallest_pair = (a, b)

    return tuple(sorted(smallest_pair))

def prod(arr):
    ret = 1
    for a in arr:
        ret *= a
    return ret

def ans(n):
    f = sieve.factorize(n)
    f = sorted(f)
    if len(f) == 1:
        return (1, n-1)
    # print("f=", f)
    a = prod(f[1:])
    b = n - a
    return (a, b)

# for i in range(2, 1000000):
#     # print(i, ans(i), ans_slow(i))
#     assert(ans(i) == ans_slow(i))
# exit(0)

T = int(input())

for t in range(T):
    n = int(input())
    print(*ans(n))