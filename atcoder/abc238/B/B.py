#!/usr/bin/env pypy3

import io, os
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

input()
A = read_int_list()

prefixes = [0]
for a in A:
    prefixes += [prefixes[-1] + a]

prefixes = [p % 360 for p in prefixes]
prefixes.sort()

gaps = []
for i in range(len(prefixes)):
    gaps += [prefixes[(i+1) % len(prefixes)] - prefixes[i]]

gaps = [g % 360 for g in gaps]

print(max(gaps))