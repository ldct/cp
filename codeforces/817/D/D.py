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
    scores = []
    optimal = []
    for i, c in enumerate(S):
        if c == 'L':
            scores += [i]
        else:
            scores += [len(S)-i-1]

        optimal += [max(i, len(S)-i-1)]

    gap = [b - a for (a,b) in zip(scores, optimal)]

    gap = sorted(gap)[::-1]
    ret = [sum(scores)]

    for g in gap:
        ret += [ret[-1] + g]

    return ret[1:]

for _ in range(read_int()):
    input()
    print(*ans(input()))