#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

MODULUS = 10**9+7

### CODE HERE

def is_monotone(p):
    for i in range(len(p)-2):
        x, y, z = p[i:i+3]
        if x < y < z: return False
        if x > y > z: return False
    return True

def splice(p, i):
    return tuple(p[0:i] + p[i+1:])

def score_pos(p, i):
    return is_monotone(splice(p, i))

def score(p):
    ret = 0
    for i in range(len(p)):
        if score_pos(p, i):
            ret += 1
    return ret

@lru_cache(None)
def ans(tup):
    N = len(tup)

    if N == 3 and is_monotone(tup):
        return 6

    indexes = []

    for i in range(N):
        if score_pos(tup, i):
            indexes += [i]

    if len(indexes) == 1:
        i = indexes[0]
        return ans(splice(tup, i)) % MODULUS

    if len(indexes) == 2:
        return (3*pow(2, N-2, MODULUS)) % MODULUS

    ret = 0
    for i in indexes:
        ret += ans(splice(tup, i))

    return (ret % MODULUS)

# for N in range(3, 10):
#     for p in permutations(range(1, N+1)):
#         if is_monotone(p):
#             print(p, ans(p))
for _ in range(read_int()):
    input()
    print(ans(read_int_tuple()))