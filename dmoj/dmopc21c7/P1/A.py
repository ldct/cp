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

N, M = read_int_tuple()
arr = []
for _ in range(N):
    arr += [read_int_list()]

def get(i, j):
    if not (0 <= i < N): return -1
    if not (0 <= j < M): return -1
    return arr[i][j]

arr[0][0] = max(arr[0][0], 1)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            arr[i][j] = 1 + max(
                get(i-1, j),
                get(i, j-1)
            )
        else:
            if not max(
                get(i-1, j),
                get(i, j-1)
            ) < arr[i][j]:
                print(-1)
                sys.exit(0)

for row in arr:
    print(*row)
