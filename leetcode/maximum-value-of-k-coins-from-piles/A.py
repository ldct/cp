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

def maxValueOfCoins(piles, k):
    def p(arr):
        ret = [0]
        for a in arr:
            ret += [ret[-1] + a]
        return ret

    def merge(A, B):
        ret = [0]*min(k+1, len(A)+len(B))
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                if i + j < (k+1):
                    ret[i+j] = max(ret[i+j], a+b)
        return ret
    piles = [p(a) for a in piles]

    ret = piles[0]
    for pile in piles[1:]:
        ret = merge(ret, pile)
    return ret[k]

piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]
k = 7

print(maxValueOfCoins(piles, k))