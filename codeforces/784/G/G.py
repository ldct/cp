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

def fall(row):
    ret = ['.']*len(row)
    obstacles = []
    cnt = 0
    for i, c in enumerate(row):
        if c == '.': continue
        elif c == 'o':
            obstacles += [(i, cnt)]
            cnt = 0
        elif c == '*':
            cnt += 1
    if cnt > 0:
        for i in range(cnt):
            ret[len(ret)-i-1] = '*'

    for j, cnt in obstacles:
        ret[j] = 'o'
        for i in range(cnt):
            ret[j - i - 1] = '*'

    return ret

def ans(grid):
    grid = list(zip(*grid))
    grid = [fall(row) for row in grid]
    grid = list(zip(*grid))

    for row in grid:
        print(''.join(row))
    print()

for _ in range(read_int()):
    n, m = read_int_tuple()
    grid = []
    for _ in range(n):
        grid += [list(input())]
    ans(grid)