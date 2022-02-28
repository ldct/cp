#!/usr/bin/env pypy3

import io, os
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


def total(freq):
        return freq['.'] + freq['#']

def ok_row(row):
    if len(row) < 6: return False
    freq = defaultdict(int)
    i = 0
    while total(freq) != 6:
        freq[row[i]] += 1
        i += 1

    while True:
        if freq['.'] <= 2: return True
        if i == len(row): return False

        freq[row[i]] += 1
        freq[row[i-6]] -= 1

        i += 1

def off_diag(grid):
    ret = []
    for _ in range(len(grid) + len(grid[0]) - 1):
        ret += [[]]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            ret[x+y] += [grid[x][y]]

    return ret

def ok(grid):
    for row in grid:
        if ok_row(row): return "Yes"

    grid = list(zip(*grid))
    for row in grid:
        if ok_row(row): return "Yes"

    od = off_diag(grid)
    for row in od:
        if ok_row(row): return "Yes"

    grid = [row[::-1] for row in grid]
    od = off_diag(grid)
    for row in od:
        if ok_row(row): return "Yes"


    return "No"

N = read_int()
grid = [input() for _ in range(N)]
print(ok(grid))