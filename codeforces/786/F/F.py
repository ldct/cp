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

n, m, q = read_int_tuple()
grid = [input() for _ in range(n)]
num_icons = ''.join(grid).count('*')
grid = list(zip(*grid))
grid = list(map(list, grid))

dp = 0
for i in range(num_icons):
    x = i // n
    y = i % n
    if grid[x][y] == '*':
        dp += 1

def coord(t):
    return t//n, t%n

for _ in range(q):
    y, x = read_int_tuple()
    x -= 1
    y -= 1
    if grid[x][y] == '.':
        # add an element
        if x*n+y < num_icons: dp += 1

        i, j = coord(num_icons)
        num_icons += 1

        grid[x][y] = '*'
        if grid[i][j] == '*': dp += 1


    else:
        if x*n+y < num_icons: dp -= 1

        num_icons -= 1
        i, j = coord(num_icons)

        grid[x][y] = '.'
        if grid[i][j] == '*': dp -= 1



    print(num_icons - dp)