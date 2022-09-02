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

def ans(grid):

    if '***' in "n".join(grid): return "NO"
    g2 = list(zip(*grid))
    if '***' in "n".join(''.join(row) for row in g2): return "NO"

    grid = list(map(list, grid))

    R = len(grid)
    C = len(grid[0])

    for x in range(R):
        for y in range(C):
            for dx, dy in [(+1, +1), (-1, -1), (+1, -1), (-1, +1)]:
                new_x = x + dx
                new_y = y + dy
                if not (0 <= new_x < R): continue
                if not (0 <= new_y < C): continue

                if grid[x][y] == '*' and grid[new_x][new_y] == '*':
                    a = grid[x][new_y]
                    b = grid[new_x][y]

                    if a+b == '*.': continue
                    if a+b == '.*': continue
                    return 'NO'

    for x in range(R):
        for y in range(C):
            for dx, dy in [(+1, +1), (-1, -1), (+1, -1), (-1, +1)]:
                new_x = x + dx
                new_y = y + dy
                if not (0 <= new_x < R): continue
                if not (0 <= new_y < C): continue

                if grid[x][y] == '*' and grid[new_x][new_y] == '*':
                    grid[x][new_y] = '.'
                    grid[new_x][y] = '.'
                    grid[x][y] = '.'
                    grid[new_x][new_y] = '.'

    for row in grid:
        if '*' in row: return 'NO'
        # print(row)

    return 'YES'

for _ in range(read_int()):
    R, C = read_int_tuple()
    print(ans([input() for _ in range(R)]))