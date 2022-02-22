#!/usr/bin/env pypy3

import io, os
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

def dist2(p, q):
    return p*p + q*q

def ans(x, y, X, Y):
    for xx in range(X-10, X+10):
        for yy in range(Y-10, Y+10):
            if dist2(x - xx, y - yy) == 5 and dist2(X - xx, Y - yy) == 5:
                return True
    return False

x, y, X, Y = read_int_list()
print("Yes" if ans(x, y, X, Y) else "No")
