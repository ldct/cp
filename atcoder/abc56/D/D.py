#!/usr/bin/env python3

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

def ss_ncp(target, B):
    import array
    possible = array.array('b', [1] + [0]*target)

    for b in B:
        for mass in range(target, -1, -1):
            if possible[mass] == 1 and mass + b <= target:
                possible[mass+b] = 1
    return possible

### CODE HERE

N, K = read_int_tuple()
A = read_int_list()

A = [min(a, K+1) for a in A]

assert(N <= 400)
assert(K <= 400)

ret = 0

for i in range(len(A)):
    T = K + max(A)
    x = A[i]
    B = list(A)
    del B[i]
    p = ss_ncp(T, B)
    good = False
    for w in range(len(p)):
        if not p[w]: continue
        if w < K <= w+x:
            good = True
    if not good:
        ret += 1

print(ret)