#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import math
from functools import lru_cache

import operator as op
from functools import reduce, lru_cache

def comb(n, r):
    if r > n: return 0
    if r == 0: return 1
    if r == 1: return n
    if r == 2: return n*(n-1)//2
    return reduce(op.mul, range(n - r + 1, n + 1), 1) // math.factorial(r)


def count_partitions_interval(size, _sum=None, l=0, r):

    if _sum is None: _sum = r

    n = size
    N = _sum
    """
    Number of tuples x_1, x_2 ... x_n such that
    x_i \in [l, r]
    \sum x_i = N
    """

    N -= n*l
    r -= l

    ret = 0
    UB = min(n, N // (r+1))
    for q in range(0, 1+UB):
        ret += (-1)**q * comb(n, q) * comb(N - q*(r+1) + n-1, n-1)
    return ret

N, K = read_int_tuple()

def c3(S, N):
    return count_partitions_interval(size=3, _sum=S, l=1, r=N)

def c2(S, N):
    return count_partitions_interval(size=2, _sum=S, l=1, r=N)

for S in range(3, 10**100):
    # if S % 100 == 0: print(S)
    if K > c3(S, N):
        K -= c3(S, N)
    else:
        break

for s in range(S-1, -1, -1):
    if K > c2(s, N):
        K -= c2(s, N)
    else:
        break

def ans2(s, K):
    candidates = []
    for a in range(1, N+1):
        if 1 <= s-a <= N and 1 <= a <= N:
            candidates += [(a, s-a)]
    return candidates[K-1]

a,b = ans2(s, K)
print(S-s, a, b)
