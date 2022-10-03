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

class PrefixSum:
    def __init__(self, lst):
        self.lst = lst
        self.p = [0]
        for e in lst:
            self.p += [self.p[-1] + e]
            
    def sum(self, i, j):
        return self.p[j] - self.p[i]

N, M = read_int_tuple()
A = read_int_list()

L = [a*(i+1) for (i, a) in enumerate(A)]

pA = PrefixSum(A)
pL = PrefixSum(L)

def score(i, j):
    return pL.sum(i, j) - i*pA.sum(i, j)

ret = float("-inf")

for i in range(len(A) - M + 1):
    # print(score(i, i+M))
    ret = max(ret, score(i, i+M))

print(ret)
