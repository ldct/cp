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

cs_of = []
for p in range(30):
    cs = [0]
    for i in range(2*10**5+1):
        if (2**p & i):
            cs += [cs[-1] + 1]
        else:
            cs += [cs[-1]]
    cs_of += [cs]

def overlap(l, r, p):
    return cs_of[p][r+1] - cs_of[p][l]

def ans(l, r):
    best = max(overlap(l, r, p) for p in range(30))
    return r - l + 1 - best

for _ in range(read_int()):
    l, r = read_int_list()
    print(ans(l, r))