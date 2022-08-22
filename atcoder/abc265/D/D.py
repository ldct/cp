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

N, P, Q, R = read_int_list()
A = read_int_list()
haystack = [0]
for a in A:
    haystack += [haystack[-1] + a]

def find(e):
    j = bisect_left(haystack, e)
    if 0 <= j < len(haystack) and haystack[j] == e:
        return j
    return None

def ans():
    for i in range(len(haystack)):
        j = find(haystack[i] + P)
        if j is None: continue
        k = find(haystack[j] + Q)
        if k is None: continue
        l = find(haystack[k] + R)
        if l is None: continue
        return "Yes"
    return "No"

print(ans())