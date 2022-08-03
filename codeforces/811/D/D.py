#!/usr/bin/env python3

import io, os, sys
from sys import stdin, stdout
from typing import List

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

def videoStitching(clips, T):
    ret = []
    end, end2, res = -1, 0, 0
    for i, j, idx in sorted(clips):
        if end2 >= T or i > end2:
            break
        elif end < i <= end2:
            # print("using", i, j, idx)
            res += 1
            end = end2
            ret += [(idx, i)]
            end2 = max(end2, j)
        if j > end2:
            end2 = j
            ret.pop()
            ret += [(idx, i)]
    return ret if end2 >= T else -1

def ans(t: str, ss: List[str]):
    intervals = []
    for si, s in enumerate(ss):
        for i in range(len(t)):
            if t[i:i+len(s)] == s:
                intervals += [(i, i+len(s), si)]

    ret = videoStitching(intervals, len(t))
    if ret == -1: 
        print(-1)
        return

    print(len(ret))

    for (idx, p) in ret:
        print(idx + 1, p + 1)

for _ in range(read_int()):
    t = input()
    s = [input() for _ in range(read_int())]
    ans(t, s)