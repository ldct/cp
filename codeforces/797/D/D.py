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

def ans(K, cells):
    cells = [(1 if cells[i] == 'B' else 0) for i in range(len(cells))]

    candidates = []

    rs = sum(cells[0:K])
    candidates += [rs]

    for i in range(len(cells) - K):
        rs -= cells[i]
        rs += cells[K+i]
        candidates += [rs]

    return K - max(candidates)

for _ in range(read_int()):
    N, K = read_int_tuple()
    cells = input()

    print(ans(K, cells))