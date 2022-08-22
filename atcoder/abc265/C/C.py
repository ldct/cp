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

H, W = read_int_list()
grid = [input() for _ in range(H)]

x = 0
y = 0
for i in range(H*W*5+100):
    if i == H*W*5+10:
        old_pair = (-1,)
        break
    old_pair = (x+1, y+1)
    if grid[x][y] == 'U':
        x -= 1
    elif grid[x][y] == 'D':
        x += 1
    elif grid[x][y] == 'L':
        y -= 1
    elif grid[x][y] == 'R':
        y += 1
    
    if not ((0 <= x < H) and (0 <= y < W)):
        break

print(*old_pair)