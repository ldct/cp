#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import random
from collections import defaultdict
from functools import lru_cache

### CODE HERE

def mean(f):
    sample = [f() for _ in range(10**5)]
    return sum(sample) / len(sample)

def ans_very_slow(n, m):
    def trial():
        big_pool = list(range(n))*m
        small_pool = random.sample(big_pool, n)
        return 1.0 if random.choice(small_pool) == random.choice(small_pool) else 0.0

    return mean(trial)

def runs_sample(arr):
    freq = defaultdict(int)
    for a in arr: freq[a] += 1
    ret = 0
    for k in freq:
        ret += freq[k]**2
    return ret

def runs_slow(n, m):
    def trial():
        big_pool = list(range(n))*m
        small_pool = random.sample(big_pool, n)
        return runs_sample(small_pool)
    return mean(trial)

def exp_x2(k, a, b):
    # Exp[X^2 | X = number of 1's drawn from a pool of a 1's and b 0's ]

    def trial():
        pool = [1]*a + [0]*b
        X = sum(random.sample(pool, k))
        return X**2

    return mean(trial)

def dp_x(k, a, b):
    # Exp[X | X = number of 1's drawn from a pool of a 1's and b 0's ]
    return k*a/(a+b)

@lru_cache(None)
def dp_x2(k, a, b):
    # Exp[X^2 | X = number of 1's drawn from a pool of a 1's and b 0's ]
    if k == 0: return 0.0
    if b == 0: return k**2
    if a == 0: return 0.0

    total = a+b

    a_exp = dp_x2(k-1, a-1, b) + 2*dp_x(k-1, a-1, b) + 1
    b_exp = dp_x2(k-1, a, b-1)

    # w.p. a/total, you will select a 1, and Exp((X+1)^2) = Exp(X^2) + 2Exp(X) + 1
    ret = a/total * a_exp + b/total * b_exp

    return ret

def runs(n, m):
    total = n*m
    good = m
    return dp_x2(n, good, total-good)

def ans(n, m):
    return runs(n, m) / n

print(ans(*read_int_list()))