#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
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

intervals_starting = defaultdict(list)

N, Q = read_int_tuple()
for _ in range(Q):
    l, r = read_int_tuple()
    intervals_starting[l-1] += [r]

for i in range(N):
    intervals_starting[i].sort()
    last = i
    # print(i, intervals_starting[i])
    for j in intervals_starting[i]:
        if last < j and last != i:
            intervals_starting[last] += [j]
        last = j

for i in intervals_starting:
    intervals_starting[i] = [t for t in intervals_starting[i] if t != i]


i = 0
while True:
    t = intervals_starting[i]
    if len(t) == 0: break
    i = min(t)

print("Yes" if i == N else "No")