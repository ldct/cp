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

### CODE HERE

def ans(N, K, mex):
    if mex > K: return [-1]

    ret = [-1]*N

    for i in range(K):
        if i < mex:
            ret[i] = i
        else:
            ret[i] = 0

    for i in range(N):
        if ret[i] == -1:
            ret[i] = ret[i - K]

    return ret

for _ in range(read_int()):
    N, K, X = read_int_tuple()
    print(*ans(N, K, X))