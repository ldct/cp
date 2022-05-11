#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import itertools
from functools import lru_cache

def prod(arr):
    ret = 1
    for a in arr:
        ret *= a
    return ret

def interesting(N):
    S = str(N)
    A = 1
    for c in S:
        A *= int(c)
    return (A % sum(map(int, S))) == 0

def num_interesting_slow(N):
    ret = 0
    for i in range(1, N):
        if interesting(i):
            ret += 1
    return ret

@lru_cache(None)
def num_interesting_digits(r):
    if r == 0: return 0

    ret = num_interesting_digits(r-1)
    for d in range(1, 10):
        ret += num_interesting_dp(d, d, r-1)
    return ret

@lru_cache(None)
def num_interesting_dp(s, p, r):
    if r == 0:
        if s == 0 and p == 0: return 0
        if p % s == 0:
            return 1
        else:
            return 0
    if p == 0 and s == 0: return num_interesting_digits(r)
    ret = 0
    for x in range(0, 10):
        S = s + x
        P = p * x
        ret += num_interesting_dp(S, P, r-1)
    return ret

@lru_cache(None)
def num_interesting(N):
    N = list(map(int, str(N)))

    ret = 0
    for i in range(len(N)):
        prefix = N[0:i]
        x = N[i]
        rest = len(N) - len(prefix) - 1

        for j in range(x):
            r = num_interesting_dp(
                sum(prefix) + j,
                prod(prefix) * j,
                rest
            )
            if r is not None: ret += r
    return ret

def ans(a, b):
    return num_interesting(b+1) - num_interesting(a)

T = int(input())
for t in range(T):
    a, b = read_int_tuple()
    print("Case #" + str(t+1) + ": " + str(ans(a, b)))
