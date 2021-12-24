#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

### CODE HERE

def ans_slow(N, M, K):
    p = []
    candidates = []
    for x in range(0, K+1):
        y = K - x
        candidates += [((N//(x+1))*(M//(y+1)), x, y)]
        p += [(x+1)*(y+1)]
    # print(candidates)
    return max(candidates)[0]

def ans(N, M, K):
    p = []
    candidates = []
    low = K + 1 - M
    high = N - 1

    if not (low <= high): return -1

    low = max(0, low)
    high = min(high, K)

    for x in [low, high]:
        y = K - x
        if not x >= 0: continue
        if not y >= 0: continue
        candidates += [(N//(x+1))*(M//(y+1))]

    ret = max(candidates)
    if ret == 0: return -1
    return ret

if False:
    N, M, K = 13,2,2
    print(ans_slow(N, M, K))
    print(ans(N, M, K))
elif False:
    for N in range(1, 100):
        for M in range(1, 100):
            for K in range(1, 100):
                if not ans(N, M, K) == ans_slow(N, M, K):
                    print(N, M, K)
elif True:
    print(ans(*read_int_list()))