#!/usr/bin/env python3

from email.policy import default
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
from heapq import *

### CODE HERE

cost = defaultdict(int)
neighbours = defaultdict(list)

N, M = read_int_list()
A = read_int_list()
for _ in range(M):
    u, v = read_int_list()
    u -= 1
    v -= 1

    neighbours[u] += [v]
    neighbours[v] += [u]
    cost[u] += A[v]
    cost[v] += A[u]

entries = []
for i in range(N):
    heappush(entries, (cost[i], i))

ret = 0

deleted = set()

while len(entries):
    c, u = heappop(entries)
    if u in deleted:
        continue
    if cost[u] == c:
        deleted.add(u)
        ret = max(ret, c)
        for v in neighbours[u]:
            cost[v] -= A[u]
            heappush(entries, (cost[v], v))

print(ret)
