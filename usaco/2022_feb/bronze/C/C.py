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

N = read_int()
dices = [input() for _ in range(4)]
S = ""
perms = list(permutations(dices))
indices_lst = list(product(range(0, 6), repeat=4))

strings = []
for p in perms:
    for indices in indices_lst:
        s = zip(p, indices)
        s = ''.join([a[b] for (a, b) in s])
        strings += [s]

S = '_'.join(strings)

for _ in range(N):
    haystack = input()
    print("YES" if haystack in S else "NO")
