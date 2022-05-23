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

N, A, B = read_int_tuple()

grid = []
for _ in range(A*N):
    row = ["?"]*(B*N)
    grid += [row]

for i in range(A*N):
    for j in range(B*N):
        X = i // A
        Y = j // B

        if (X + Y) % 2 == 0:
            grid[i][j] = "."
        else:
            grid[i][j] = "#"

for row in grid:
    print("".join(row))