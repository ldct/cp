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

def ans(H, W, R, C):
    ret = 0
    if R > 1: ret += 1
    if R != H: ret += 1
    if C > 1: ret += 1
    if C != W: ret += 1
    return ret

H, W = read_int_tuple()
R, C = read_int_tuple()
print(ans(H, W, R, C))