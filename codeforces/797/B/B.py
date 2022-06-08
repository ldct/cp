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

def ans(A, B):
    gap = max(a - b for (a, b) in zip(A, B))

    if gap < 0: return "NO"
    A = [max(0, a - gap) for a in A]

    if A == B: return "YES"
    return "NO"
    return A, B, gap

for _ in range(read_int()):
    input()
    A = read_int_list()
    B = read_int_list()
    print(ans(A, B))