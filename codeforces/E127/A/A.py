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

def ans(S):

    S += '$'

    splitted = []
    last = ""
    for c in S:
        if last == "":
            last = c
        elif last[-1] == c:
            last += c
        else:
            splitted += [last]
            last = c

    for s in splitted:
        if len(s) == 1: return "NO"

    return "YES"

    return S, splitted

for _ in range(read_int()):
    print(ans(input()))