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

s = input()

def unbalanced(x):
    if not (len(x) >= 2): return False
    for c in x:
        if x.count(c) * 2 > len(x): return True
    return False

def ans(s):
    for i in range(len(s)):
        if unbalanced(s[i:i+2]):
            return i+1, i+2
        elif unbalanced(s[i:i+3]):
            return i+1, i+3

    return -1, -1

print(*ans(s))