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

N, A = read_int_list()
X = read_int_list()

@lru_cache(None)
def ans(i, cnt, total):
    if i == len(X):
        if (cnt, total) == (0, 0): return 1
        return 0

    ret = ans(i+1, cnt, total) + ans(i+1, cnt-1, total-X[i])
    return ret

ret = 0
for cnt in range(1, len(X)+1):
    ret += ans(0, cnt, cnt*A)

print(ret)