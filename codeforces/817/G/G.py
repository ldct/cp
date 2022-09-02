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

import random

### CODE HERE

def ans(N):
    ret = set()
    while len(ret) != N-1:
        ret.add(random.randint(0, 2**30))
    ret = list(ret)
    last = 0
    for r in ret:
        last ^= r

    ret += [last]
    assert(len(set(ret)) == len(ret))
    return ret

for _ in range(read_int()):
    print(*ans(read_int()))