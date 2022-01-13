#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def fprint(*args):
	print(*args, flush=True)

N = read_int()
total_added = 0

possibilities = list(range(1, N+1))

while True:
    if len(possibilities) == 1:
        fprint(f"! {possibilities[0]}")
        break
    length = possibilities[-1] - possibilities[0] + 1

    to_start = N - length // 2
    start = possibilities[0] % N
    to_add = to_start - start
    if to_add <= 0:
        to_add += N

    fprint(f"+ {to_add}")
    res = int(input())

    possibilities = [p + to_add for p in possibilities]

    possibilities = [p for p in possibilities if p // N == res]
