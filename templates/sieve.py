#!/usr/bin/env python3

"""
factors = sieve()
factors[9] = 3
factors[10] = 2
factors[11] = -1

n       time    memory
10^7    300ms   140 MB
"""
def sieve(n=10**7):
    s = [-1] * n
    for i in range(2, int(n**0.5)+1):
        if s[i] != -1: continue
        for j in range(i, n, i): 
            if j > i: s[j] = i
    return s

def primes(n=10**7):
    factors = sieve(n)
    return [i for i, e in enumerate(factors) if e == -1 and i >= 2]

primes()