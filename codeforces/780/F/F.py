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

def tail(S):

    ret = 0

    last_minus = 0

    low = 0
    height = 0

    for c in S:
        if c == '-':
            last_minus += 1
            low -= 1
            if last_minus % 2 == 0:
                height += 1

        else:
            last_minus = 0
            low += 1

        if low <= 0 <= low+3*height:
            if (-low) % 3 == 0:
                ret += 1
        # print(low, height)
    return ret

def ans(S):
    ret = 0
    for i in range(len(S)):
        ret += tail(S[i:])
    return ret

for _ in range(read_int()):
    input()
    print(ans(input()))