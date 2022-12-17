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

### CODE HERE

N, M = read_int_tuple()
A = read_int_list()
M = len(A)

# apply swap(b, b+1) to a
def c(a, b):
    if a == b:
        return b+1
    elif a == b+1:
        return b
    return a

prefixes = [1]
for i in range(len(A)):
    prefixes += [c(prefixes[-1], A[i])]

# for i in range(M):
#     print(f"i={i}", A[0:i], prefixes[i], A[i+1:])

forward = dict()

suffix = []

ret = []

for i, p in enumerate(A[::-1]):

    e = prefixes[len(prefixes)-2-i]
    # print(suffix, forward, e, forward.get(e, e))

    ret += [forward.get(e, e)]

    q = p+1
    p_ = forward.get(p, p)
    q_ = forward.get(q, q)
    forward[p] = q_
    forward[q] = p_
    suffix += [p]

for r in ret[::-1]:
    print(r)