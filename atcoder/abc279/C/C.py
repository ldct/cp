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

H, W = read_int_tuple()
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

S = list(zip(*S))
T = list(zip(*T))

# print(sorted(S))
# print(sorted(T))

if sorted(S) == sorted(T):
    print("Yes")
else:
    print("No")
