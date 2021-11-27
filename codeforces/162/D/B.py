#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

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

    def fastfactorize(self, n, exclude_duplicates=True):
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

def ans(A):
    A = sorted(list(set(A)))
    # print(A)
    MAX_A = max(A) + 1

    best_prime = [0]*MAX_A
    ret = [0]*MAX_A

    for a in A:
        ps = sieve.fastfactorize(a)
        ret[a] = 1
        for p in ps:
            ret[a] = max(ret[a], 1+best_prime[p])
        for p in ps:
            best_prime[p] = max(best_prime[p], ret[a])

    return max(ret)

input()
print(ans(read_int_list()))