#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE


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

def ans(L, R):
    N = R + 100

    sigma = [0]*N
    for i in range(1, N):
        for j in range(i, N, i):
            if i >= L:
                sigma[j] += 1

    phi = [0]*N
    phi[0] = 0
    phi[1] = 1
    for i in range(2, N):
        phi[i] = i

    for i in range(2, N):
        if sieve.isprime(i):
            for j in range(i, N, i):
                phi[j] -= phi[j]//i


    phi_low = [0]*N
    phi_low[0] = 0
    phi_low[1] = 1
    for i in range(L, N):
        phi_low[i] = L

    for i in range(2, L+1):
        if sieve.isprime(i):
            for j in range(i, N, i):
                phi_low[j] -= phi_low[j]//i

    L += 1

    # print(phi[L:L+5])
    # print(phi_low[L:L+5])

    def f1(y):
        # number of x in [L, R] s.t. x, y coprime and x < y
        return phi[y] - phi_low[y]

    def f2(y):
        # number of x in [L, R] s.t. x | y and x < y
        return sigma[y] - 1

    ret = 0

    for y in range(L, R+1):
        # print(y, y-L, "-", f1(y), "-", f2(y), '=', y-L-f1(y)-f2(y))
        ret += y - L
        ret -= f1(y)
        ret -= f2(y)

    if L == 1:
        ret += R

    return 2*ret

def ans_slow(L, R):
    ret = 0
    for x in range(L, R+1):
        for y in range(L, R+1):
            g = math.gcd(x, y)
            if g > 1 and g != x and g != y: ret += 1
    return ret


def f(L, x):
    ret = 0
    for i in range(1, L+1):
        if math.gcd(i, x) == 1:
            ret += 1
    return ret

print(f(9, 8))
print(f(9, 5))
print(f(100, 40))

# for L in range(1, 10):
#     for a in range(1, 10):
#         for b in range(1, 10):
#             if math.gcd(a, b) == 1 and f(L, a*b) != f(L, a)*f(L, b):
#                 print(L, a, b)
