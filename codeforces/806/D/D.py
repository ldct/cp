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

def ans(S):
    parts = set(S)
    def f(s):
        for i in range(1, len(s)):
            if s[0:i] in parts and s[i:] in parts:
                return '1'
        return '0'
    ret = [f(s) for s in S]
    return ''.join(ret)

for _ in range(read_int()):
    N = read_int()
    strings = [input() for _ in range(N)]
    print(ans(strings))