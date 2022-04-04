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

N, K = read_int_tuple()
arr = read_int_list()
arr.sort()
ret = arr[K-1]
if K == 0:
    if arr[0] > 1:
        print(1)
    else:
        print(-1)
else:
    if len([a for a in arr if a <= ret]) == K:
        print(ret)
    else:
        print(-1)
