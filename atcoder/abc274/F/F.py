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

N, A = read_int_list()
fishes = [read_int_tuple() for _ in range(N)]

for i in range(len(fishes)):
    [W, X, V] = fishes[i]
    other_fishes = fishes[0:i] + fishes[i+1:]
    other_fishes = [(w, x-X, v-V) for (w, x, v) in other_fishes]
    print(other_fishes)
