#!/usr/bin/env pypy3

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

def ans(A, queries):
    A = sorted(A)[::-1]
    p = [0]
    for a in A:
        p += [p[-1] + a]

    for q in queries:
        r = bisect_left(p, q)
        if r == len(p):
            r = -1
        print(r)

for _ in range(read_int()):
    n, q = read_int_tuple()
    A = read_int_list()
    queries = [read_int() for _ in range(q)]

    ans(A, queries)