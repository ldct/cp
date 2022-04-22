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

def parr(arr):
    ret = [0]
    for a in arr:
        ret += [ret[-1] + a]
    return ret

def ans(arr):
    total = sum(arr)
    forward = parr(arr)
    backward = parr(arr[::-1])

    bid = dict()
    for j, b in enumerate(backward):
        bid[b] = j

    best = 0

    for i in range(len(forward)):
        # alice eats i
        eat = forward[i]

        if eat*2 > total: break

        if eat in bid:
            j = bid[eat]

            best = i+j
            # print(i, j)

    return best

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))