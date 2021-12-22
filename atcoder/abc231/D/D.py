#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

### CODE HERE

N, M = read_int_tuple()
deg = defaultdict(int)
for _ in range(M):
    a, b = read_int_tuple()
    a -= 1
    b -= 1
    deg[a] += 1
    deg[b] += 1

def ans():
    for k in deg:
        if deg[k] > 2: return "No"

    visited = [False]*N

    for i in range(N):


    return "Yes"

# visited = [N]

print(ans())
